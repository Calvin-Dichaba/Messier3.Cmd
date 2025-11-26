# Data Acquisition Notes

The photometric data used to construct the Colour Magnitude Diagram (CMD) for **Messier 3** was obtained from the **PanSTARRS DR2 (PS1)** online catalogue.

## How the Data Was Obtained

1. Queried the Pan-STARRS DR2 catalogue for sources in the field around **Messier 3**.
2. Selected the photometric bands:
   - `g`
   - `i`
3. Downloaded the resulting catalogue as a CSV file.
4. Opened the CSV in Excel.
5. Computed the color index:
g-i = g_mag - i_mag
6. Exported the cleaned two-column dataset (`g`, `g-i`) for plotting in the CMD.

## Note

The original dataset is not included in this repository due to size considerations and PanSTARRS redistribution rules.  
Users wishing to reproduce the dataset may obtain it by querying PanSTARRS DR2 via the public online query tools (MAST or PS1 catalogue access).

## Pan-STARRS DR2 Catalogue Access

Users can reproduce the dataset by querying the public Pan-STARRS DR2 archive:

- MAST Pan-STARRS Query Tool: https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
- PS1 CasJobs (SQL interface): https://mastweb.stsci.edu/ps1casjobs/
