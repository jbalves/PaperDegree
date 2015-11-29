% legend_str = {'SMO' 'J48' 'REP Tree' 'Naive Bayes' 'Random Tree' 'Zero R'};
% plot(q_inst,resultsy,'.-','MarkerSize',17);
% l1 = columnlegend(3,legend_str, 'Location', 'BestOutside', 'boxoff');
% legend(l1);
% xlabel('Instâncias');
% ylabel('TP Rate');
% l1_pos = get(l1,'Position');
% l1_pos(1,1)=0.25;
% l1_pos(1,2)=0.6780;
% set(l1,'Position',l1_pos);
% print(gcf,'tp_graph','-dpng');
% 
% figure();
% plot(q_inst,resultsx,'.-','MarkerSize',17);
% l2 = columnlegend(3,legend_str, 'Location', 'BestOutside', 'boxoff');
% legend(l2);
% xlabel('Instâncias');
% ylabel('FP Rate');
% set(l2,'Position',l1_pos);
% print(gcf,'fp_graph','-dpng');

str_legend = {'SMO' 'J48' 'REPT' 'NB' 'RT' 'ZR'};
qdata=size(p_right,2);
qlines = size(p_right,1);
for i=1:qdata
    g = bar([p_right(:,i) ones(qlines,1)*100-p_right(:,i)],0.9,'stacked');
    legend('Acertos','Erros','Location','BestOutSide');
    set(gca,'XTickLabel',str_legend);
    ylim([0 101]);
    xlabel('Algoritmo');
    ylabel('Porcentagem (%)');
    print(gcf,sprintf('perc_hits_%dk',i*5),'-dpng');
end