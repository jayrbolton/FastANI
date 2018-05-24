# import multiprocessing
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil

# Fetch genome assemblies in parallel


def fetch_multiple(callback_url, refs):
    """
    Fetch multiple assembly files in parallel and return them in an array
    :param callback_url:
    :param refs: array of workspace references to assemblies
    :returns: array of file paths of fetched assemblies
    """
    assembly_util = AssemblyUtil(callback_url)
    # pool = multiprocessing.Pool(processes=2)
    # jobs = []
    results = []
    for ref in refs:
        results.append(fetch_assembly(assembly_util, ref))
    # for ref in refs:
    #     jobs.append(pool.apply_async(fetch_assembly, (assembly_util, ref)))
    # return [j.get() for j in jobs]
    return results


def fetch_assembly(assembly_util, ref):
    """ Fetch a single assembly file with a workspace reference """
    x = assembly_util.get_assembly_as_fasta({'ref': ref})
    print('!?!?!?', x)
    return x['path']
