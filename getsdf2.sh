#!/bin/sh

#echo $1
mysql --quick -N -h localhost -uroot  -e 'select distinct c.molfile,"> <MOLREGNO>",'$1',"\n" "$$$$" from  compound_structures c where c.molregno = '$1'\G' chembl_19 | grep -v "row" >> drug.sdf

# echo $2
# mysql --quick -N -h localhost -uroot -e 'select distinct c.molfile,"> <MOLREGNO>",'$2',"\n" "$$$$" from  compound_structures c where c.molregno = '$2'\G' chembl_19  >> kk

#grep -v "row" kk >drug.sdf
#rm kk
