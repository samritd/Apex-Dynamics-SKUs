import csv

def generate_apex_af_afr_skus():
    """
    Generates SKUs for Apex Dynamics AF and AFR series planetary gearboxes
    based on the provided specifications, excluding unavailable combinations,
    and saves them to separate CSV files (one for AF, one for AFR).
    """

    # --- Define parameters for AF Series ---
    af_sizes = [
        "AF042", "AF060", "AF060A", "AF075", "AF075A",
        "AF100", "AF100A", "AF140", "AF140A", "AF180", "AF220"
    ]
    af_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10]
    af_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 50, 60, 70, 80, 90, 100
    ]
    af_ratios = sorted(list(set(af_ratios_1_stage + af_ratios_2_stage)))

    # Define explicitly unavailable AF Series combinations based on Page 4 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_af_combinations = set()
    for ratio in af_ratios_1_stage:
        if ratio == 7: # Specific unavailable for AF075A
            unavailable_af_combinations.add(("AF075A", ratio))
        # These models have all 1-stage ratios unavailable
        if ratio in [3,4,5,6,7,8,9,10]: # All 1-stage ratios
            unavailable_af_combinations.add(("AF060A", ratio))
            unavailable_af_combinations.add(("AF100A", ratio))
            unavailable_af_combinations.add(("AF140A", ratio))
            unavailable_af_combinations.add(("AF180", ratio))
            unavailable_af_combinations.add(("AF220", ratio))


    # --- Define parameters for AFR Series ---
    abr_sizes = [
        "AFR042", "AFR060", "AFR060A", "AFR075", "AFR075A",
        "AFR100", "AFR100A", "AFR140", "AFR140A", "AFR180", "AFR220"
    ]
    afr_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20]
    afr_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 48, 50, 60, 64, 70, 80,
        90, 100, 120, 140, 160, 180, 200
    ]
    afr_ratios = sorted(list(set(afr_ratios_1_stage + afr_ratios_2_stage)))

    # Define explicitly unavailable AFR Series combinations based on Page 8 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_afr_combinations = set()

    # Unavailable 1-stage ratios for specific models
    for ratio in afr_ratios_1_stage:
        unavailable_afr_combinations.add(("AFR060A", ratio))
        unavailable_afr_combinations.add(("AFR075A", ratio))
        unavailable_afr_combinations.add(("AFR100A", ratio))
        unavailable_afr_combinations.add(("AFR140A", ratio))

    # Specific unavailable 1-stage ratios for AFR180 and AFR220
    unavailable_afr_combinations.add(("AFR180", 6))
    unavailable_afr_combinations.add(("AFR180", 12))
    unavailable_afr_combinations.add(("AFR220", 6))
    unavailable_afr_combinations.add(("AFR220", 12))

    # Unavailable 2-stage ratios for specific models (12, 15, 16, 20)
    for ratio in [12, 15, 16, 20]:
        unavailable_afr_combinations.add(("AFR042", ratio))
        unavailable_afr_combinations.add(("AFR060", ratio))
        unavailable_afr_combinations.add(("AFR060A", ratio))
        unavailable_afr_combinations.add(("AFR075", ratio))
        unavailable_afr_combinations.add(("AFR075A", ratio))
        unavailable_afr_combinations.add(("AFR100", ratio))
        unavailable_afr_combinations.add(("AFR100A", ratio))
        unavailable_afr_combinations.add(("AFR140", ratio))
        unavailable_afr_combinations.add(("AFR140A", ratio))

    # Unavailable 2-stage ratios for specific models (120, 140, 160, 180, 200)
    for ratio in [120, 140, 160, 180, 200]:
        unavailable_afr_combinations.add(("AFR042", ratio))
        unavailable_afr_combinations.add(("AFR060", ratio))
        unavailable_afr_combinations.add(("AFR060A", ratio))
        unavailable_afr_combinations.add(("AFR075", ratio))
        unavailable_afr_combinations.add(("AFR075A", ratio))
        unavailable_afr_combinations.add(("AFR100", ratio))
        unavailable_afr_combinations.add(("AFR100A", ratio))
        unavailable_afr_combinations.add(("AFR140", ratio))
        unavailable_afr_combinations.add(("AFR140A", ratio))


    # Common parameters for both series
    shaft_options = ["S1", "S2", "S3"]
    backlash_options = ["P0", "P1", "P2"]

    af_skus = []
    afr_skus = []

    # Generate SKUs for AF Series
    for size in af_sizes:
        for ratio in af_ratios:
            if (size, ratio) in unavailable_af_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    af_skus.append(["AF Series", size, formatted_ratio, shaft, backlash, sku])

    # Generate SKUs for AFR Series
    for size in abr_sizes: # Note: using abr_sizes for AFR series
        for ratio in afr_ratios:
            if (size, ratio) in unavailable_afr_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    afr_skus.append(["AFR Series", size, formatted_ratio, shaft, backlash, sku])

    # --- Write SKUs to separate CSV files ---
    af_csv_file_name = "apex_dynamics_af_skus.csv"
    afr_csv_file_name = "apex_dynamics_afr_skus.csv"

    # Write AF SKUs
    with open(af_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(af_skus)
    print(f"Successfully generated {len(af_skus)} AF Series SKUs and saved to '{af_csv_file_name}'")

    # Write AFR SKUs
    with open(afr_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(afr_skus)
    print(f"Successfully generated {len(afr_skus)} AFR Series SKUs and saved to '{afr_csv_file_name}'")

# Run the SKU generation function
generate_apex_af_afr_skus()
