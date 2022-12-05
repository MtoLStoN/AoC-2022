#!/bin/zsh

input=$1
declare -i count_compl
declare -i count_atall
count_compl=0
count_atall=0

while read -r line; do
   elf1=$(echo $line | gawk -F "," '{print $1}')
   elf2=$(echo $line | gawk -F "," '{print $2}')
   elf1_lower=$(echo $elf1 | gawk -F "-" '{print $1}')
   elf1_higher=$(echo $elf1 | gawk -F "-" '{print $2}')
   elf2_lower=$(echo $elf2 | gawk -F "-" '{print $1}')
   elf2_higher=$(echo $elf2 | gawk -F "-" '{print $2}')

   is_true=$(echo $elf1_lower $elf1_higher $elf2_lower $elf2_higher | gawk '{
   if (($3 <= $1 && $4 >= $2) || ($1 <= $3 && $2 >= $4)) 
      print "TRUE"
   else 
      print "FALSE"
   }
   ')

   if [[ $is_true == "TRUE" ]]; then
      count_compl=count_compl+1
   fi

   is_true="FALSE"

   is_true=$(echo $elf1_lower $elf1_higher $elf2_lower $elf2_higher | gawk '{
   if (($4 < $1)  || ($3 > $2)) 
      print "TRUE"
   else 
      print "FALSE"
   }
   ')

   if [[ $is_true == "TRUE" ]]; then
      count_atall=count_atall+1
   fi

   is_true="FALSE"
done < $input

echo "No Overlap: "$count_atall
echo "Some Overlap: "$(echo $count_atall | gawk '{print 1000-$1}')
echo "Complete Overlap: "$count_compl
