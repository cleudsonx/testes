#!/usr/bin/env python
# -*- coding:UTF-8 -*-

usuario = "rafael"
password = "1234"

login = raw_input ("Digite seu login de usuário: ")
senha = raw_input ("Digite sua senha: ")

if (login == usuario) and (senha == password):
    print "Autenticação realizada com Sucesso!"
    print "Sistema de de validação de usuário!"
else:
    print "Acesso Negado!!!!"