from django.db import models

class SurveyResponse(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)  # Allow null values for age
    gender = models.CharField(max_length=10, null=True)  # Allow null values for gender
    country = models.CharField(max_length=100, null=True)  # Allow null values for country
    state = models.CharField(max_length=100, blank=True, null=True)  # Allow null values for state
    self_employed = models.CharField(max_length=3, null=True)  # Allow null values for self_employed
    family_history = models.CharField(max_length=3, null=True)  # Allow null values for family_history
    treatment = models.CharField(max_length=3, null=True)  # Allow null values for treatment
    work_interfere = models.CharField(max_length=20, null=True)  # Allow null values for work_interfere
    no_employees = models.CharField(max_length=20, null=True)  # Allow null values for no_employees
    remote_work = models.CharField(max_length=3, null=True)  # Allow null values for remote_work
    tech_company = models.CharField(max_length=3, null=True)  # Allow null values for tech_company
    benefits = models.CharField(max_length=20, null=True)  # Allow null values for benefits
    care_options = models.CharField(max_length=20, null=True)  # Allow null values for care_options
    wellness_program = models.CharField(max_length=20, null=True)  # Allow null values for wellness_program
    seek_help = models.CharField(max_length=20, null=True)  # Allow null values for seek_help
    anonymity = models.CharField(max_length=20, null=True)  # Allow null values for anonymity
    leave = models.CharField(max_length=20, null=True)  # Allow null values for leave
    mental_health_consequence = models.CharField(max_length=20, null=True)  # Allow null values for mental_health_consequence
    phys_health_consequence = models.CharField(max_length=20, null=True)  # Allow null values for phys_health_consequence
    coworkers = models.CharField(max_length=20, null=True)  # Allow null values for coworkers
    supervisor = models.CharField(max_length=20, null=True)  # Allow null values for supervisor
    mental_health_interview = models.CharField(max_length=20, null=True)  # Allow null values for mental_health_interview
    phys_health_interview = models.CharField(max_length=20, null=True)  # Allow null values for phys_health_interview
    mental_vs_physical = models.CharField(max_length=20, null=True)  # Allow null values for mental_vs_physical
    obs_consequence = models.CharField(max_length=3, null=True)  # Allow null values for obs_consequence
    comments = models.TextField(blank=True, null=True)  # Allow null values for comments

    def __str__(self):
        return f"Survey Response #{self.id} - {self.timestamp}"
