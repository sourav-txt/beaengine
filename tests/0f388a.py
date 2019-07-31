#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):

        # EVEX.128.66.0F38.W0 8a /r
        # vcompressps xmm2/m128 {k1}{z}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompressps ')
        assert_equal(myDisasm.instr.repr, 'vcompressps xmmword ptr [rsi], xmm1')

        # EVEX.256.66.0F38.W0 8a /r
        # vcompressps ymm2/m256 {k1}{z}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompressps ')
        assert_equal(myDisasm.instr.repr, 'vcompressps ymmword ptr [rsi], ymm1')

        # EVEX.512.66.0F38.W0 8a /r
        # vcompressps zmm2/m512 {k1}{z}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompressps ')
        assert_equal(myDisasm.instr.repr, 'vcompressps zmmword ptr [rsi], zmm1')

        # EVEX.128.66.0F38.W1 8a /r
        # vcompresspd  xmm2/m128 {k1}{z},xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompresspd ')
        assert_equal(myDisasm.instr.repr, 'vcompresspd xmmword ptr [rsi], xmm1')

        # EVEX.256.66.0F38.W1 8a /r
        # vcompresspd ymm2/m256 {k1}{z},ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompresspd ')
        assert_equal(myDisasm.instr.repr, 'vcompresspd ymmword ptr [rsi], ymm1')

        # EVEX.512.66.0F38.W1 8a /r
        # vcompresspd zmm2/m512 {k1}{z}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}8a0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x8a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcompresspd ')
        assert_equal(myDisasm.instr.repr, 'vcompresspd zmmword ptr [rsi], zmm1')