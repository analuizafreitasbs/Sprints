diretorio_relatorios="vendas/backup"


arquivo_saida="relatorio_fina.txt"


num_execucoes=$(ls -l $diretorio_relatorios | grep -c relatorio)

if [ $num_execucoes -ge 1 ]; then

    rm -f $arquivo_saida


    cat $diretorio_relatorios/relatorio*.txt >> $arquivo_saida

    echo "Relatórios consolidados com sucesso em $arquivo_saida"
else
    echo "Não há relatórios suficientes para consolidar. Pelo menos três execuções do script processamento_de_vendaas.sh são necessárias."
fi
