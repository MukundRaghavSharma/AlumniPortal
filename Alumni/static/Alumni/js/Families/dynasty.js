function Dynasty() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['<a href="/profile/3"Imee Chan</a>',''',''],
['<a href="/profile/16"Daniel Kim</a>',''',''],
['<a href="/profile/24"Melanie Mui</a>',''',''],
['<a href="/profile/41"Anna Ly</a>','<a href="/profile/18"Ellen Lai</a>', ''],
['<a href="/profile/57"Lu Zhang</a>','<a href="/profile/24"Melanie Mui</a>', ''],
['<a href="/profile/76"Jason Ma</a>','<a href="/profile/41"Anna Ly</a>', ''],
['<a href="/profile/104"Scarlett Su</a>','<a href="/profile/41"Anna Ly</a>', ''],
['<a href="/profile/105"Konstantin Vidensky</a>','<a href="/profile/57"Lu Zhang</a>', ''],
['<a href="/profile/121"Hugo Zhang</a>','<a href="/profile/76"Jason Ma</a>', ''],
['<a href="/profile/125"Alvin Poh</a>','<a href="/profile/104"Scarlett Su</a>', ''],
['<a href="/profile/130"Stephanie Yue</a>','<a href="/profile/121"Hugo Zhang</a>', ''],
['<a href="/profile/148"Ahmad Shamsuddin</a>','<a href="/profile/121"Hugo Zhang</a>', ''],
['<a href="/profile/165"Zachary Rousselle</a>','<a href="/profile/105"Konstantin Vidensky</a>', ''],
['<a href="/profile/184"Nathaniel Eliason</a>','<a href="/profile/165"Zachary Rousselle</a>', ''],
['<a href="/profile/189"Dixon Liang</a>','<a href="/profile/148"Ahmad Shamsuddin</a>', ''],
['<a href="/profile/231"Alvin Mathew</a>','<a href="/profile/184"Nathaniel Eliason</a>', ''],
['<a href="/profile/236"Yvonne Yuan</a>','<a href="/profile/189"Dixon Liang</a>', ''],
['<a href="/profile/238"Nathaniel Benzaquen-Ouakrat</a>','<a href="/profile/165"Zachary Rousselle</a>', ''],
['<a href="/profile/245"Shreeyagya Khemka</a>','<a href="/profile/184"Nathaniel Eliason</a>', ''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('dynasty_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        