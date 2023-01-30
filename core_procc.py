# -*- coding: utf-8 -*-

"""
############################# OFTEN OWN FILE core.py #########################
"""
import Userdict


class cmd_pak(Userdict):
    
    def func_name(*args, **kwargs):
        pass
    def method_name(self, *args, **kwargs):
        pass


# i = argvs.index(arg)
# arg == 1 or arg == 'ON' or arg == 'true' or arg == 'True'
#this only handles argument flags
class cmd_flag_parser:
    def __call__(self,*argvs):
        
        #having the list thing here makes it static.. so only ONE exist no matter how many
        #"cmd_parser instances you create.. this may not be inded in which case make an 
        #__init__(cls) and place it cls.map[]
        L_cmdz_map = []
        for arg in argvs:
            if arg == 'start':
                    L_cmdz_map['start'] = True
            if arg == 'R_tests':
                L_cmdz_map['R_tests'] = True
        return L_cmdz_map
    
    
class Process:
    
    def __init__(cls, cmd_line_start_args):
        
        # thus this map here is just a pointer (well a name alais, to that static vayable!
        #which you can localy acess in this fucntion)
           L_cmdz_map=  cmd_flag_parser(cmd_line_start_args)
        #orrr if you do this, it is a local process owned instance of that but it points to the orginal static not a copy. 
        cls.L_cmdz_map = cmd_parser(cmd_line_start_args)
                  
    @staticmethod
    def Help():
        print("YOUR IN PROCESS HELP; you must entre arguments. valid arguments are:\n",
              "INPUT_FILE",           
              "if you provide a -o followed by output path otherwise defults to the dir /out here\n")
    
    #this is for cmds hadling after the program is already running!
    @classmethod        
    def handle_terminal_cmds(cls, incmdpak):
        pass 
   
   @classmethod 
   def cyclework():
       if Process.L_cmdz_map["R_tests"] == True:
           print("you shold be runnign tests!")
    
"""############################# end of  core.py #########################
"""   

class enumerate I_types:
    
class pyars_checker:
    
    def __call__(self, pyfile):
        
        pattern_IMPORT_MODUAL_YYYY = r"^import\w+ ]"
        m_name = " "
        pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY  =r"(?<=from )(\w+:?\s?)(?:.*import):?\s?(:?\s?.*:?\s?)" # (?P<m_name> w\+) 
        
        
       "\w*(?<from )(\w+)"
        # (?<=from )(\w+\s?)
        # r"(?<=from )(\w+\s?)(?:.*import)(.*)"
        
      import_mod_list = pyfile.findall(pattern_IMPORT_MODUAL_YYYY)  
      import_func_from_mod_list = pyfile.findall(pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY)  
      
      
import re 
sample_py = '''import modual_YYY \
from modual1  import funcozmmmm, other, func3 
from modual2 import someoth2, andagianfunc
sskshix_oth wordfs 2023-01-28.'''
m_name = " "
#(?<=from )(\w+\s?)
pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY  = r"(?<=from )(\w+:?\s?)(?:.*import):?\s?(:?\s?.*:?\s?)"  #(?<=from )(\w+)(\w+) # (?P<m_name> w\+) 
#.*[.].*$
outfound =  re.findall(pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY, sample_py)
import_func_modual_map = {}
for moudals in outfound:
    modualname = moudals[0]
    for mfuncs in moudals:
        func_callist = []
        for rmf in mfuncs.split(","):
            func_callist.append(rmf.strip())
    import_func_modual_map[modualname] =  func_callist 

print(import_func_modual_map)
m = re.match(r'(?<=from )(?P<m_name>\w+) (?P<next>\w+)',sample_py)

    
      
      
      def pars_iffm_list(mlist):
          for it in mlist:
              it[0]
          
      
      def gen_exdtrnal_func_serch_list(import_mod_list,import_func_from_mod_list):
          pattern_EXTERNALl_FUNC__EXE = r"{}".format()
          
      
      excute_ext_func_list = 
      
      
      import re 
sample_py = '''import modual_YYY \
from modual1  import funcozmmmm 
sskshix_oth wordfs 2023-01-28.'''
m_name = " "

pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY  = r"(?<=from)((\w+)\s?)(.?import)[\w+]"  #(?<=from )(\w+)(\w+) # (?P<m_name> w\+) 

outfound =  re.findall(pattern_IMPORT_FUNC_PPP_FROM_MODUAL_YYY, sample_py)
for line in outfound :
    print(line)
print(m_name)

m = re.match(r'(?<=from )(?P<m_name>\w+) (?P<next>\w+)',sample_py)

class injest():
    
    
    def __call__(self,**kwargss):
      
        if kwargss["type"] == :
            
            dotfiles 
    
    imported_funcs,
    imported_modulas
    class_names,
    function_names:free,Member,
    
    
   output_formate =  pypars_checker(pyfile)
    
   
    
    