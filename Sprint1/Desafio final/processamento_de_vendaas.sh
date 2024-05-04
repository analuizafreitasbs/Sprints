cp dados_de_vendas.csv vendas/

data_execucao=$(date +%Y%m%d)

mkdir vendas/backup


cp dados_de_vendas.csv vendas/backup/dados-$data_execucao.csv


mv vendas/backup/dados-$data_execucao.csv vendas/backup/backup-dados-$data_execucao.csv

data_sistema=$(date +"%Y/%m/%d %H:%M")

primeira_data=$(awk -F',' 'NR==2{print $5}' vendas/backup/backup-dados-$data_execucao.csv)


ultima_data=$(awk -F',' 'END{print $5}' vendas/backup/backup-dados-$data_execucao.csv)

total_itens=$(awk -F',' 'NR>1{print $2}' vendas/backup/backup-dados-$data_execucao.csv | sort | uniq | wc -l)


echo "Data do sistema: $data_sistema" > vendas/backup/relatorio.txt
echo "Data do primeiro registro de venda: $primeira_data" >> vendas/backup/relatorio.txt
echo "Data do último registro de venda: $ultima_data" >> vendas/backup/relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $total_itens" >> vendas/backup/relatorio.txt


head -n 10 vendas/backup/backup-dados-$data_execucao.csv >> vendas/backup/relatorio.txt


zip vendas/backup/backup-dados-$data_execucao.zip vendas/backup/backup-dados-$data_execucao.csv

echo "Processamento de vendas concluído!"
