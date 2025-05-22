import csv

def generate_apex_afx_afxr_skus():
    """
    Generates SKUs for Apex Dynamics AFX and AFXR series planetary gearboxes
    based on the provided specifications, excluding unavailable combinations,
    and saves them to separate CSV files (one for AFX, one for AFXR).
    """

    # --- Define parameters for AFX Series ---
    afx_sizes = [
        "AFX042", "AFX060", "AFX060A", "AFX075", "AFX075A",
        "AFX100", "AFX100A", "AFX140", "AFX140A", "AFX180"
    ]
    afx_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10]
    afx_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 50, 60, 70, 80, 90, 100
    ]
    afx_ratios = sorted(list(set(afx_ratios_1_stage + afx_ratios_2_stage)))

    # Define explicitly unavailable AFX Series combinations based on Page 4 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_afx_combinations = set()

    # Models with all 1-stage ratios unavailable
    for ratio in afx_ratios_1_stage:
        unavailable_afx_combinations.add(("AFX060A", ratio))
        unavailable_afx_combinations.add(("AFX075A", ratio))
        unavailable_afx_combinations.add(("AFX100A", ratio))
        unavailable_afx_combinations.add(("AFX140A", ratio))
        unavailable_afx_combinations.add(("AFX180", ratio))

    # Specific unavailable ratios
    unavailable_afx_combinations.add(("AFX100", 6))
    unavailable_afx_combinations.add(("AFX140", 6))


    # --- Define parameters for AFXR Series ---
    afxr_sizes = [
        "AFXR042", "AFXR060", "AFXR060A", "AFXR075", "AFXR075A",
        "AFXR100", "AFXR100A", "AFXR140", "AFXR140A", "AFXR180"
    ]
    afxr_ratios_1_stage = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20]
    afxr_ratios_2_stage = [
        12, 15, 16, 20, 25, 28, 30, 32, 35, 40, 45, 48, 50, 60, 64, 70, 80,
        90, 100, 120, 140, 160, 180, 200
    ]
    afxr_ratios = sorted(list(set(afxr_ratios_1_stage + afxr_ratios_2_stage)))

    # Define explicitly unavailable AFXR Series combinations based on Page 8 of the PDF
    # Format: (Gearbox Size, Ratio)
    unavailable_afxr_combinations = set()

    # Models with all 1-stage ratios unavailable
    for ratio in afxr_ratios_1_stage:
        unavailable_afxr_combinations.add(("AFXR060A", ratio))
        unavailable_afxr_combinations.add(("AFXR075A", ratio))
        unavailable_afxr_combinations.add(("AFXR100A", ratio))
        unavailable_afxr_combinations.add(("AFXR140A", ratio))

    # Specific unavailable 1-stage ratios
    unavailable_afxr_combinations.add(("AFXR180", 8))
    unavailable_afxr_combinations.add(("AFXR060", 12))
    unavailable_afxr_combinations.add(("AFXR075", 12))
    unavailable_afxr_combinations.add(("AFXR100", 12))
    unavailable_afxr_combinations.add(("AFXR140", 12))

    # Unavailable 2-stage ratios
    for ratio in [12, 15, 16, 20]:
        unavailable_afxr_combinations.add(("AFXR042", ratio))
        unavailable_afxr_combinations.add(("AFXR060", ratio))
        unavailable_afxr_combinations.add(("AFXR060A", ratio))
        unavailable_afxr_combinations.add(("AFXR075", ratio))
        unavailable_afxr_combinations.add(("AFXR075A", ratio))
        unavailable_afxr_combinations.add(("AFXR100", ratio))
        unavailable_afxr_combinations.add(("AFXR100A", ratio))
        unavailable_afxr_combinations.add(("AFXR140", ratio))
        unavailable_afxr_combinations.add(("AFXR140A", ratio))

    for ratio in [120, 140, 160, 180, 200]:
        unavailable_afxr_combinations.add(("AFXR042", ratio))
        unavailable_afxr_combinations.add(("AFXR060", ratio))
        unavailable_afxr_combinations.add(("AFXR060A", ratio))
        unavailable_afxr_combinations.add(("AFXR075", ratio))
        unavailable_afxr_combinations.add(("AFXR075A", ratio))
        unavailable_afxr_combinations.add(("AFXR100", ratio))
        unavailable_afxr_combinations.add(("AFXR100A", ratio))
        unavailable_afxr_combinations.add(("AFXR140", ratio))
        unavailable_afxr_combinations.add(("AFXR140A", ratio))


    # Common parameters for both series
    shaft_options = ["S1", "S2", "S3"]
    backlash_options = ["P0", "P1", "P2"]

    afx_skus = []
    afxr_skus = []

    # Generate SKUs for AFX Series
    for size in afx_sizes:
        for ratio in afx_ratios:
            if (size, ratio) in unavailable_afx_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    afx_skus.append(["AFX Series", size, formatted_ratio, shaft, backlash, sku])

    # Generate SKUs for AFXR Series
    for size in afxr_sizes:
        for ratio in afxr_ratios:
            if (size, ratio) in unavailable_afxr_combinations:
                continue
            for shaft in shaft_options:
                for backlash in backlash_options:
                    formatted_ratio = f"{ratio:03d}"
                    sku = f"{size}-{formatted_ratio}-{shaft}-{backlash}"
                    afxr_skus.append(["AFXR Series", size, formatted_ratio, shaft, backlash, sku])

    # --- Write SKUs to separate CSV files ---
    afx_csv_file_name = "apex_dynamics_afx_skus.csv"
    afxr_csv_file_name = "apex_dynamics_afxr_skus.csv"

    # Write AFX SKUs
    with open(afx_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(afx_skus)
    print(f"Successfully generated {len(afx_skus)} AFX Series SKUs and saved to '{afx_csv_file_name}'")

    # Write AFXR SKUs
    with open(afxr_csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Series", "Gearbox Size", "Ratio", "Shaft Option", "Backlash", "SKU"])
        csv_writer.writerows(afxr_skus)
    print(f"Successfully generated {len(afxr_skus)} AFXR Series SKUs and saved to '{afxr_csv_file_name}'")

# Run the SKU generation function
generate_apex_afx_afxr_skus()
