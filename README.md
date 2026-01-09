# T3DB - Toxin and Toxin-Target Database

T3DB is a comprehensive resource containing detailed information about common toxins and their biological targets. It includes pollutants, pesticides, drugs, food toxins, and metabolites that can be harmful to humans.

## Data Source

- **Original Database**: T3DB (Wishart Lab, University of Alberta)
- **Website**: https://www.t3db.ca/
- **Reference**: Lim et al., Nucleic Acids Research, 2010
- **License**: Free for academic use, commercial use requires permission

## Database Statistics

- ~3,678 toxins with detailed annotations
- ~2,073 toxin target records
- Over 90 data fields per toxin record

## Output Files

| File | Description |
|------|-------------|
| `brick/toxins.parquet` | All toxin records with chemical properties, toxicity values, and metadata |
| `brick/targets.parquet` | Toxin target proteins and genes |
| `brick/mechanisms_of_action.parquet` | Toxin-target interaction mechanisms and references |
| `brick/structures.parquet` | Chemical structures in parsed SDF format |

## Usage

```r
# R
biobricks::install_brick("t3db")
biobricks::brick_pull("t3db")
t3db <- biobricks::brick_load("t3db")
```

```python
# Python
import biobricks as bb
bb.install("t3db")
toxins = bb.load("t3db", "toxins")
```

## Key Data Fields

### Toxins
- Chemical name, synonyms, CAS number
- SMILES, InChI, molecular formula
- Toxicity values (LD50, LC50)
- Exposure routes, health effects
- Target organs, mechanisms

### Targets
- UniProt ID, gene name
- Protein/gene sequences
- Species
- Associated toxins

## Applications

- Environmental toxicology research
- Drug safety assessment
- Chemical risk analysis
- Toxin mechanism studies
- Biomarker discovery

## Citation

Lim E, et al. T3DB: a comprehensively annotated database of common toxins and their targets. Nucleic Acids Res. 2010;38:D781-D786.
