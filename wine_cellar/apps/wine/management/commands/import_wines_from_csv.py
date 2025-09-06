import csv
import ast
from django.core.management.base import BaseCommand
from wine_cellar.apps.wine.models import Wine, Vineyard, Grape, Classification, FoodPairing, Size, Source

class Command(BaseCommand):
    help = 'Imports wines from a specified CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import.')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        self.stdout.write(f"Importing wines from {csv_file_path}...")

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Get or create related objects first
                vineyard, _ = Vineyard.objects.get_or_create(name=row['WineryName'], defaults={'country': row['Code']})
                size, _ = Size.objects.get_or_create(name=1.0)

                # Step 1: Create the main Wine object WITHOUT the ManyToManyField
                wine, created = Wine.objects.get_or_create(
                    name=row['WineName'],
                    # The 'vineyard' field is removed from this section
                    defaults={
                        'wine_type': row['Type'].split('/')[0][:2].upper(),
                        'country': row['Code'],
                        'abv': float(row['ABV']) if row['ABV'] else None,
                        'size': size
                    }
                )

                if created:
                    # Step 2: AFTER the wine is created, add the vineyard to the relationship
                    wine.vineyard.add(vineyard)

                    # Add other Many-to-Many relationships
                    grape_names = ast.literal_eval(row.get('Grapes', '[]'))
                    for name in grape_names:
                        grape, _ = Grape.objects.get_or_create(name=name.strip())
                        wine.grapes.add(grape)

                    food_names = ast.literal_eval(row.get('Harmonize', '[]'))
                    for name in food_names:
                        food, _ = FoodPairing.objects.get_or_create(name=name.strip())
                        wine.food_pairings.add(food)

                    self.stdout.write(self.style.SUCCESS(f'Successfully created wine: {wine.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Wine already exists, skipping: {wine.name}'))

        self.stdout.write(self.style.SUCCESS('Finished importing wines.'))