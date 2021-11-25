:: For loop to iterate over each region - update absolute path with repo location
for %%f in (C:\Users\kenne\Developer\CSC782TermProject\inputs\regions\*) do (
    python graphs.py regions %%~nf
    )

:: For loop to iterate over each event - update absolute path with repo location
for %%f in (C:\Users\kenne\Developer\CSC782TermProject\inputs\events\*) do (
    python graphs.py events %%~nf
    )