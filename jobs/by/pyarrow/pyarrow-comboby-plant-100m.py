import pyarrow.dataset as ds

def bench_definition(output_prefix_path):
    df = ds.dataset(output_prefix_path + '/data/relation-no-nulls-100m.parquet', format='parquet').to_table().select(['plant_id', 'Values']).to_pandas()
    def after():
        nonlocal df
        del df
    def do():
        g = df.groupby(['plant_id']).agg(Count=('Values', 'count'), Average=('Values', 'mean'), Std=('Values', 'std'))
        return len(g.index)
    bench_name = 'pyarrow-comboby-plant'
    return (bench_name, do, after)
