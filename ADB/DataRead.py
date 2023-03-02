# Databricks notebook source
diamonds_df = (spark.read
  .format("csv")
  .option("mode", "PERMISSIVE")
  .load("/Workspace/Repos/rajatrath872@gmail.com/AzureAutomations/ADB/annual-enterprise-survey-2021-financial-year-provisional-csv.csv")
)
