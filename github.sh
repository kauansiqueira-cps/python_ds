#!/bin/sh

#Altere as variáveis abaixo de acordo com a sua necessidade
#na variável repositório, prefira a url do repositório baseada em https para nao termos que configurar SSH
export name='kauansiqueira-cps'
export email="kauan.siqueira@etec.sp.gov.br"
export repositorio=" https://github.com/kauansiqueira-cps/python_ds.git";

#Daqui pra baixo mexa somente se for realmente necessário ou se souber o que está fazendo :P

export branch_name="aula-$(date +%d%m)-Prova"

rm -Rf .git

git init
git remote add origin $repositorio
git checkout -b $branch_name

git config --global user.name $name
git config --global user.email $email

git add .

git commit -am "branch com o código da aula do dia $(date)"

git push origin $branch_name