#!/usr/bin/env python
# -*- coding:UTF-8 -*-

usuario = "rafael"
password = "1234"

login = raw_input ("Digite seu login de usu�rio: ")
senha = raw_input ("Digite sua senha: ")

if (login == usuario) and (senha == password):
    print "Usuario autenticado com sucesso!"
    print "Seja Bem Vindo ao Sistema!"
else:
    print "Negado!!!!"