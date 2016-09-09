#!/usr/bin/env python
# -*- coding: gbk -*-
# File Name: dicConvert.py
# Author: weitao
# mail: weitao@sogou-inc.com
# Created Time: 2016��04��29�� ������ 16ʱ01��08��
# ToDo:convert word to word(start,middle,end,single) format
# For Example:
# Pw @ 2016-04-29 16:01:08
import os
import re
import sys

# 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)

import codecs
import sys

def character_tagging(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + "/S ")
            else:
                output_data.write(word[0] + "/B ")
                for w in word[1:len(word)-1]:
                    output_data.write(w + "/M ")
                output_data.write(word[len(word)-1] + "/E ")
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please use: python character_tagging.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_tagging(input_file, output_file)