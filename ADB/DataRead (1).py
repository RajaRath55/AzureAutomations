# Databricks notebook source
diamonds_df = (spark.read
  .format("csv")
  .option("mode", "PERMISSIVE")
  .load("/FileStore/tables/annual_enterprise_survey_2021_financial_year_provisional_csv.csv")
)
