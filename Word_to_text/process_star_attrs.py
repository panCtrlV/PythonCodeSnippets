'''
Process MS word files in the following folders to prepare a list of STAR attributes and their description.

    K:\Core Risk Modeling\Portfolio Risk Modeling\STAR_Attributes_Definitions

But this can be generalize to parse and extract information from any Word documents.

This script was first developed on Windows 7 and Python 3.6.

# Shell Command Tool DocTo
The DocTo tool (windows shell command to convert Word doc to text) can be downloaded from: 

    https://github.com/tobya/DocTo/releases

Its usage can be found at:

    http://tobya.github.io/DocTo/
    

@author: panc
@date: 2017-07-06
'''

from subprocess import STDOUT, check_output, TimeoutExpired
import glob
import os, sys
import re


if __name__=='__main__':
    txt_available = False  # if all Word docs have already been converted to txt

    # Location of the docto.exe (Windows CL tool we downloaded to convert Word doc to txt)
    home_dir = '</home/dir/path>'

    # Directory of Word docs
    word_doc_dir = '<word_doc_dir_name>'

    # File to save the compiled attr code and description
    outfname = '<output_file_name>.csv'
    outfpath = os.path.join(home_dir, outfname)
    with open(outfpath, 'w') as outf:
        outf.write('attr_code,attr_description\n')

    if not txt_available:
        # Word docs have not been converted yet

        # Get the name list of the Word docs
        fpath_lst = glob.glob( home_dir + '/' + word_doc_dir + '/S*.doc*' )

        # Temp file to save text
        txt_temp_fname = '<temp_file_name>.temp'
        txt_temp_fpath = os.path.join(home_dir, txt_temp_fname)

        with open(outfpath, 'a') as outf:
            for i, fpath in enumerate(fpath_lst):
                try:
                    # Convert a word doc to txt by running a shell command.
                    cmd = home_dir+'docto.exe -f \"' + fpath + '\" -O \"' + txt_temp_fpath + '\" -T wdFormatText'
                    output = check_output(cmd, shell=True, stderr=STDOUT, timeout=5)  # 'timeout' only works for Python 3 ?

                    with open(txt_temp_fname, 'r') as txtf:
                        for line in txtf.readlines():
                            if line.startswith('Short Name:'):
                                attr_code = line.split(':')[1].strip()
                            elif line.startswith('Long Name:'):
                                attr_dscr = re.sub( r'^S[0-9]+\s+|$', '', line.split(':')[1].strip() ).strip()
                    
                    # Save the formatted attr code + description
                    attr_and_dscr_str = ','.join([attr_code, attr_dscr])    
                    print(attr_and_dscr_str)
                    outf.write(attr_and_dscr_str+'\n')

                    # Delete temp file
                    os.remove(txt_temp_fpath)
                except KeyboardInterrupt:
                    sys.exit(1)
                except TimeoutExpired as e:
                    print('Shell command times out: %s' % e)
                    print('\t[%d] %s' % (i, fpath))
                    continue
                except:
                    print('ERROR occurred!')
                    print('\t[%d] %s' % (i, fpath))
                    continue

    else:
        # Already converted Word docs to txt files and saved in a sub-folder

        txt_dirname = '<txt_folder_name>'
        txt_dirpath = os.path.join(home_dir, txtfname)
        txt_fpath_lst = glob.glob( os.path.join(txt_dirpath, 'S*.txt') )

        with open(outfpath, 'a') as outf:
            # Process each txt file
            for i, txt_fpath in enumerate(txt_fpath_lst):
                try:
                    with open(txt_fpath, 'r') as txtf:
                        for line in txtf.readlines():
                            if line.startswith('Short Name:'):
                                attr_code = line.split(':')[1].strip()
                            elif line.startswith('Long Name:'):
                                attr_dscr = re.sub( r'^S[0-9]+\s+|$', '', line.split(':')[1].strip() ).strip()

                    # Save the formatted attr code + description
                    attr_and_dscr_str = ','.join([attr_code, attr_dscr])    
                    print(attr_and_dscr_str)
                    outf.write(attr_and_dscr_str+'\n')
                except KeyboardInterrupt:
                    sys.exit(1)
                except:
                    print('ERROR occurred!')
                    print('\t[%d] %s' % (i, fpath))
                    continue