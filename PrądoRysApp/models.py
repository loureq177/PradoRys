from django.db import models

class CsvData(models.Model):
    time = models.IntegerField()
    max_current = models.IntegerField()
    avg_current = models.IntegerField()

    def __str__(self):
        return f"Time: {self.time}, Max Current: {self.max_current}, Avg Current: {self.avg_current}"