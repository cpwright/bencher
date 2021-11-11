import pyarrow.dataset as ds

def bench_definition(output_prefix_path):
    df = ds.dataset(output_prefix_path + '/data/relation-no-nulls-100m.parquet', format='parquet').to_table().to_pandas()
    def after():
        nonlocal df
        del df
    def do():
        df['vp1'] = df['adjective_id'] + df['animal_id'] + 1
        df['vp2'] = df['adjective_id'] + df['animal_id'] + 2
        df['vp3'] = df['adjective_id'] + df['animal_id'] + 3
        df['vp4'] = df['adjective_id'] + df['animal_id'] + 4
        df['vp5'] = df['adjective_id'] + df['animal_id'] + 5
        df['vp6'] = df['adjective_id'] + df['animal_id'] + 6
        df['vp7'] = df['adjective_id'] + df['animal_id'] + 7
        df['vp8'] = df['adjective_id'] + df['animal_id'] + 8
        return len(df.index)
    bench_name = 'pyarrow-select-update-bench-no-nulls-100m'
    return (bench_name, do, after)
