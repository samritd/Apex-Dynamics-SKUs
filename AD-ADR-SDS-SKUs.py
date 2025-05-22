import csv

def generate_apex_ad_adr_ads_skus():
    """
    Generates SKUs for Apex Dynamics AD, ADR, and ADS series planetary gearboxes
    based on the provided specifications, excluding unavailable combinations,
    and saves them to separate CSV files (one for AD, one for ADR, one for ADS).
    """

    # --- Define parameters for AD Series ---
    ad_sizes = [
        "AD047", "AD064", "AD090", "AD110", "AD140", "AD200", "AD255"
    ]
    ad_ratios_1_stage = [4, 5, 7, 10]
    ad_ratios_2_stage = [
        16, 20, 21, 25, 31, 35, 40, 50, 61, 70, 91, 100
    ]
    ad_ratios = sorted(list(set(ad_ratios_1_stage + ad_ratios_2_stage)))

    # Define explicitly unavailable AD Series combinations based on Page 4 of the PDF
    # (No explicit dashes in the AD series table, so this set remains empty)
    unavailable_ad_combinations = set()


    # --- Define parameters for ADR Series ---
    adr_sizes = [
        "ADR047", "ADR064", "ADR090", "ADR110", "ADR140", "ADR200", "ADR255"
    ]
    adr_ratios_1_stage = [4, 5, 7, 10, 14, 20]
    adr_ratios_2_stage = [
        20, 25, 35, 40, 50, 70, 100, 140, 200
    ]
    adr_ratios = sorted(list(set(adr_ratios_1_stage + adr_ratios_2_stage)))

    # Define explicitly unavailable ADR Series combinations based on Page 8 of the PDF
    unavailable_adr_combinations = set()
    # 1-stage ratios that are explicitly marked with '-'
    for size in ["ADR090", "ADR110", "ADR140", "ADR200", "ADR255"]:
        unavailable_adr_combinations.add((size, 14)) # Ratio 14 is missing for these models in 1-stage

    # 2-stage ratios that are explicitly marked with '-'
    for size in ["ADR047", "ADR064", "ADR090", "ADR110"]:
        unavailable_adr_combinations.add((size, 140))
        unavailable_adr_combinations.add((size, 200))


    # --- Define parameters for ADS Series ---
    ads_sizes = [
        "ADS047", "ADS064", "ADS090", "ADS110", "ADS140", "ADS200", "ADS255"
    ]
    ads_ratios_1_stage = [4, 5, 7, 10]
    ads_ratios_2_stage = [
        16, 21, 31, 61, 91
    ]
    ads_ratios = sorted(list(set(ads_ratios_1_stage + ads_ratios_2_stage)))
    ads_shaft_options = ["S1", "S2"] # ADS has specific shaft options

    # Define explicitly unavailable ADS Series combinations based on Page 11 of the PDF
    # (No explicit dashes in the ADS series table, so this set remains empty)
    unavailable_ads_combinations = set()


    # Common parameters for all series
    backlash_options = ["P0", "P1", "P2"]

    ad_skus = []
    adr_skus = []
    ads_skus = []

    # Generate SKUs for AD Series
    for size in ad_sizes:
        for ratio in ad_ratios:
            if (size, ratio) in unavailable_ad_combinations:
                continue
            for backlash in backlash_options:
                formatted_ratio = f"{ratio:03d}"
                # AD series does not have a shaft option in the ordering code
                sku = f"{size}-{formatted_ratio}-{backlash}"
                ad_skus.append(["AD Series", size, formatted_ratio, "N/A", backlash, sku])

    # Generate SKUs for ADR Series
    for size in adr_sizes:
        for ratio in adr_ratios:
            if (size, ratio) in unavailable_adr_combinations:
                continue
            for backlash in backlash_options:
                formatted_ratio = f"{ratio:03d}"
                # ADR series does not have a shaft option in the ordering code
                sku = f"{size}-{formatted_ratio}-{backlash}"
                adr_skus.append(["ADR Series", size, formatted_ratio, "N/A", backlash, sku])

    # Generate SKUs for ADS Series
    for size in ads_sizes:
        for ratio in ads_ratios:
            if (size, ratio) in unavailable_ads_combinations:
                continue
            for shaft in ads_shaft_options:
                for backlash in backlash_options:
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    ads_skus.append(["ADS Series", size, formatted_ratio, shaft, backlash, sku])

    # --- Write SKUs to separate CSV files ---
    ad_csv_file_name = "apex_dynamics_ad_skus.csv"
    adr_csv_file_name = "apex_dynamics_adr_skus.csv"
    ads_csv_file_name = "apex_dynamics_ads_skus.csv"

    # Write AD SKUs
    with open(ad_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(ad_skus)
    print(f"Successfully generated {len(ad_skus)} AD Series SKUs and saved to '{ad_csv_file_name}'")

    # Write ADR SKUs
    with open(adr_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(adr_skus)
    print(f"Successfully generated {len(adr_skus)} ADR Series SKUs and saved to '{adr_csv_file_name}'")

    # Write ADS SKUs
    with open(ads_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(ads_skus)
    print(f"Successfully generated {len(ads_skus)} ADS Series SKUs and saved to '{ads_csv_file_name}'")

# Run the SKU generation function
generate_apex_ad_adr_ads_skus()
