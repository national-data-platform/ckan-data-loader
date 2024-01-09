import pandas as pd

def create_run_links_column(filename):
    orig_csv = pd.read_csv(filename)
    orig_csv['link'] = orig_csv['fuels_dens_surface_final_plot'].apply(lambda x: x.split('png/')[0]+'quicfire.zarr')
    orig_csv.to_csv(filename, index=False)

if __name__ == '__main__':
    create_run_links_column('resources/St._Mary_large_ensemble.csv')

