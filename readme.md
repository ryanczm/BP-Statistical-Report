# BP Statistical Review for World Energy Report

Article and writeup: https://analytic-musings.com/2024/04/01/BP-statistical-review/

Objectives - demonstrate the understanding and learn these areas by analyzing the data in this report. Report can be downloaded from BP by Googling. The excel spreadsheet link is [here](https://www.reddit.com/r/energy/comments/172x9jf/can_someone_help_me_find_bp_excel_workbook_of/). I downloaded it and manually cleaned the excel files so they can be analyzed in Pandas. The code and charts is in `oil` and `gas` respectively. 



----
* Refinery technicals - Gary book
* Refinery geography/age - refinery map - US, Europe, Russia, ME, China, India. Search
* Crude geography - Platts periodic table
* Pricing mechanisms - Big Orrin conversation/Oxford institute pricing papers
---

* Flows (where to where)
    * Crude flows
    * Product flows
    * Gas flows
    * Stocks/inventory per country
* Technicals
    * Crude composition geography
    * Refinery composition geography
    * Reserves technicals geography

# Chart List

From the excel data, we plot charts out for each selected tab. The aim is to ask "what, why, how" to understand these charts.

* Crude
    * Energy Cons - EJ
    * Energy Cons Fuel 2022 - EJ
    * Oil Reserves - BN BL
    * Oil Production - K/BL/D
    * Liquids Consumption - K/BL/D
    * Product Regional Consumption - K/BL/D
    * Spot Crude Prices - USD/BL
    * Capacity - K/BL/D
    * Throughput - K/BL/D
    * Margins - USD/BL
    * Crude Import Export - K/BL/D
    * Crude Movement 2022 - MN Tonnes
    * Product Movement 2022 - MN Tonnes
* Gas
    * Gas Reserves - TN CM 
    * Gas Production - BN CM
    * Gas Consumption - BN CM
    * Gas Prices - USD/MN BTU
    * Gas Import Exports - BN CM
    * LNG Exports - BN CM
    * LNG Imports - BN CM
    * Pipeline Trade Movements - BN CM
