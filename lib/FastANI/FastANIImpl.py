# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from utils.fast_ani_proc import run_fast_ani_pairwise
from utils.fast_ani_output import get_result_data
from utils.fetch_assembly import fetch_multiple
from utils.fast_ani_report import create_report
#END_HEADER


class FastANI:
    '''
    Module Name:
    FastANI

    Module Description:
    A KBase module: FastANI
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/jayrbolton/kbase-fastANI.git"
    GIT_COMMIT_HASH = "f842fbf019545ab417a20e6ffd224cc87b24f0a6"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR
        pass


    def fast_ani(self, ctx, params):
        """
        :param params: instance of type "FastANIParams" (fast_ani input) ->
           structure: parameter "workspace_name" of String, parameter
           "assembly_refs" of list of type "workspace_ref" (@id ws
           KBaseGenomeAnnotations.Assembly)
        :returns: instance of type "FastANIResults" (fast_ani output) ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN fast_ani
        print 'Starting FastANI function and validating parameters.'
        for name in ['workspace_name', 'assembly_refs']:
            if name not in params:
                raise ValueError('Parameter "' + name + '" is not set in input arguments')
        if isinstance(params['assembly_refs'], basestring):
            params['assembly_refs'] = [params['assembly_refs']]
        ws_name = params['workspace_name']
        # Download the assembly data
        files = fetch_multiple(self.callback_url, params['assembly_refs'])
        output_paths = run_fast_ani_pairwise(self.shared_folder, files)
        result_data = get_result_data(output_paths)
        results = create_report(self.callback_url, self.shared_folder, ws_name, result_data)
        #END fast_ani

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method fast_ani return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
