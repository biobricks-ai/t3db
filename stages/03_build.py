#!/usr/bin/env python3
"""
Build script to convert T3DB data to Parquet format.
T3DB contains toxin data with mechanisms of action and target information.
"""

import os
from pathlib import Path
import pandas as pd

def parse_sdf_to_df(sdf_path):
    """Parse SDF file to extract molecule data."""
    molecules = []
    current_mol = {}
    current_field = None

    with open(sdf_path, 'r', errors='ignore') as f:
        for line in f:
            line = line.rstrip('\n')

            if line == '$$$$':
                if current_mol:
                    molecules.append(current_mol)
                current_mol = {}
                current_field = None
            elif line.startswith('> <'):
                # Field name
                current_field = line[3:-1].strip()
            elif current_field and line.strip():
                if current_field in current_mol:
                    current_mol[current_field] += ' ' + line.strip()
                else:
                    current_mol[current_field] = line.strip()

    return pd.DataFrame(molecules)

def main():
    raw_path = Path("raw")
    brick_path = Path("brick")
    brick_path.mkdir(exist_ok=True)

    # Process toxins CSV
    toxins_csv = list(raw_path.glob("**/toxins.csv"))
    if toxins_csv:
        print(f"Processing {toxins_csv[0]}...")
        df = pd.read_csv(toxins_csv[0], low_memory=False)
        df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
        output_file = brick_path / "toxins.parquet"
        df.to_parquet(output_file, index=False)
        print(f"  - Saved {len(df)} toxins to {output_file}")

    # Process targets CSV
    targets_csv = list(raw_path.glob("**/targets.csv"))
    if targets_csv:
        print(f"Processing {targets_csv[0]}...")
        df = pd.read_csv(targets_csv[0], low_memory=False)
        df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
        output_file = brick_path / "targets.parquet"
        df.to_parquet(output_file, index=False)
        print(f"  - Saved {len(df)} targets to {output_file}")

    # Process mechanisms of action CSV
    moas_csv = list(raw_path.glob("**/moas.csv"))
    if moas_csv:
        print(f"Processing {moas_csv[0]}...")
        df = pd.read_csv(moas_csv[0], low_memory=False)
        df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
        output_file = brick_path / "mechanisms_of_action.parquet"
        df.to_parquet(output_file, index=False)
        print(f"  - Saved {len(df)} mechanisms to {output_file}")

    # Process SDF structures
    sdf_files = list(raw_path.glob("**/*.sdf"))
    if sdf_files:
        all_structures = []
        for sdf_file in sdf_files:
            print(f"Processing {sdf_file}...")
            df = parse_sdf_to_df(sdf_file)
            if not df.empty:
                all_structures.append(df)

        if all_structures:
            structures_df = pd.concat(all_structures, ignore_index=True)
            structures_df.columns = [str(c).strip().lower().replace(' ', '_') for c in structures_df.columns]
            output_file = brick_path / "structures.parquet"
            structures_df.to_parquet(output_file, index=False)
            print(f"  - Saved {len(structures_df)} structures to {output_file}")

    # Print summary
    print("\nOutput files:")
    for f in brick_path.glob("*.parquet"):
        df = pd.read_parquet(f)
        print(f"  - {f.name}: {len(df)} rows, {len(df.columns)} columns")

if __name__ == "__main__":
    main()
