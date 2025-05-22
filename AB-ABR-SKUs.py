import csv

def generate_apex_skus():
    """
    Generates SKUs for Apex Dynamics AB and ABR series planetary gearboxes
    based on the provided specifications, excluding unavailable combinations,
    and saves them to separate CSV files (one for AB, one for ABR).
    """

    # Define the parameters for AB Series
    ab_sizes = [
        "AB042", "AB060", "AB060A", "AB090", "AB090A",
        "AB115", "AB115A", "AB142", "AB142A", "AB180", "AB220"
    ]
    ab_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10]
    ab_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 50, 60, 70, 80, 90, 100
    ]
    ab_ratios = sorted(list(set(ab_ratios_1_stage + ab_ratios_2_stage))) # Combine and sort unique ratios

    # Define explicitly unavailable AB Series combinations based on Page 4 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_ab_combinations = set()
    for ratio in ab_ratios_1_stage:
        unavailable_ab_combinations.add(("AB060A", ratio))
        unavailable_ab_combinations.add(("AB090A", ratio))
        unavailable_ab_combinations.add(("AB115A", ratio))
        unavailable_ab_combinations.add(("AB142A", ratio))

    # Define the parameters for ABR Series
    abr_sizes = [
        "ABR042", "ABR060", "ABR060A", "ABR090", "ABR090A",
        "ABR115", "ABR115A", "ABR142", "ABR142A", "ABR180", "ABR220"
    ]
    abr_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20]
    abr_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 48, 50, 60, 64, 70, 80,
        90, 100, 120, 140, 160, 180, 200
    ]
    abr_ratios = sorted(list(set(abr_ratios_1_stage + abr_ratios_2_stage))) # Combine and sort unique ratios

    # Define explicitly unavailable ABR Series combinations based on Page 8 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_abr_combinations = set()

    # Unavailable 1-stage ratios for specific models
    for ratio in abr_ratios_1_stage:
        unavailable_abr_combinations.add(("ABR060A", ratio))
        unavailable_abr_combinations.add(("ABR090A", ratio))
        unavailable_abr_combinations.add(("ABR115A", ratio))
        unavailable_abr_combinations.add(("ABR142A", ratio))

    # Unavailable 2-stage ratios for specific models (12, 15, 16, 20)
    for ratio in [12, 15, 16, 20]:
        unavailable_abr_combinations.add(("ABR042", ratio))
        unavailable_abr_combinations.add(("ABR060", ratio))
        unavailable_abr_combinations.add(("ABR060A", ratio))
        unavailable_abr_combinations.add(("ABR090", ratio))
        unavailable_abr_combinations.add(("ABR090A", ratio))
        unavailable_abr_combinations.add(("ABR115", ratio))
        unavailable_abr_combinations.add(("ABR115A", ratio))
        unavailable_abr_combinations.add(("ABR142", ratio))
        unavailable_abr_combinations.add(("ABR142A", ratio))
        unavailable_abr_combinations.add(("ABR180", ratio))
        unavailable_abr_combinations.add(("ABR220", ratio))

    # Unavailable 2-stage ratios for specific models (120, 140, 160, 180, 200)
    for ratio in [120, 140, 160, 180, 200]:
        unavailable_abr_combinations.add(("ABR042", ratio))
        unavailable_abr_combinations.add(("ABR060", ratio))
        unavailable_abr_combinations.add(("ABR060A", ratio))
        unavailable_abr_combinations.add(("ABR090", ratio))
        unavailable_abr_combinations.add(("ABR090A", ratio))
        unavailable_abr_combinations.add(("ABR115", ratio))
        unavailable_abr_combinations.add(("ABR115A", ratio))
        unavailable_abr_combinations.add(("ABR142", ratio))
        unavailable_abr_combinations.add(("ABR142A", ratio))


    shaft_options = ["S1", "S2", "S3"]
    backlash_options = ["P0", "P1", "P2"]

    ab_skus = []
    abr_skus = []

    # Generate SKUs for AB Series
    for size in ab_sizes:
        for ratio in ab_ratios:
            # Skip if this combination is explicitly marked as unavailable
            if (size, ratio) in unavailable_ab_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    # Format ratio with leading zero if less than 100
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    ab_skus.append(["AB Series", size, formatted_ratio, shaft, backlash, sku])

    # Generate SKUs for ABR Series
    for size in abr_sizes:
        for ratio in abr_ratios:
            # Skip if this combination is explicitly marked as unavailable
            if (size, ratio) in unavailable_abr_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    # Format ratio with leading zero if less than 100
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    abr_skus.append(["ABR Series", size, formatted_ratio, shaft, backlash, sku])

    # Define the CSV file names
    ab_csv_file_name = "apex_dynamics_ab_skus.csv"
    abr_csv_file_name = "apex_dynamics_abr_skus.csv"

    # Write the AB SKUs to a CSV file
    with open(ab_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header row
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        # Write SKU data
        csv_writer.writerows(ab_skus)

    print(f"Successfully generated {len(ab_skus)} AB Series SKUs and saved to '{ab_csv_file_name}'")

    # Write the ABR SKUs to a CSV file
    with open(abr_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header row
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        # Write SKU data
        csv_writer.writerows(abr_skus)

    print(f"Successfully generated {len(abr_skus)} ABR Series SKUs and saved to '{abr_csv_file_name}'")

# Run the SKU generation function
generate_apex_skus()
