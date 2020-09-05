import glob
from charcoal.utils import CSV_DictHelper

directory = 'output.ibd2'
hitlist = CSV_DictHelper(f'{directory}/hit_list_for_filtering.csv', 'genome')
output_dir = f'{directory}/report'

wildcard_constraints:
    g='[a-zA-Z0-9._-]+'                   # should be everything but /

rule all:
    input:
        expand("{dir}/{g}.fig.html", dir=output_dir, g=hitlist.rows),
        f'{output_dir}/index.html'


rule make_notebook:
    input:
        '_genome-report.ipynb',
    output:
        output_dir + '/{g}.fig.ipynb'
    params:
        summary_csv = f'{directory}/genome_summary.csv',
        name = '{g}',
    shell: """
        papermill {input} - \
              -p summary_csv {params.summary_csv:q} \
              -p name {params.name:q} \
              > {output}
    """

rule make_html:
    input:
        output_dir + '/{g}.fig.ipynb',
    output:
        output_dir + '/{g}.fig.html',
    shell: """
        python -m nbconvert {input} --stdout --no-input > {output}
    """
     

rule make_index:
    input:
        'report_index.ipynb',
    output:
        f'{output_dir}/index.html',
    shell: """
        papermill {input} - -p directory {directory:q} | \
            python -m nbconvert --stdin --stdout --no-input > {output}
    """
