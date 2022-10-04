from devices import stemma_soil as stem

assert stem.get_data() != [0,0], "No data was found using the script"