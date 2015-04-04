function Family() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['<a href="/profile/2"Patrick Cao</a>',''',''],
['<a href="/profile/7"Julian Chun</a>',''',''],
['<a href="/profile/8"Chris Chyu</a>',''',''],
['<a href="/profile/15"Andrew Kiang</a>',''',''],
['<a href="/profile/29"Jennifer Suh</a>',''',''],
['<a href="/profile/51"Jay Khil</a>','<a href="/profile/15"Andrew Kiang</a>', ''],
['<a href="/profile/53"Jessica Wong</a>','<a href="/profile/29"Jennifer Suh</a>', ''],
['<a href="/profile/59"Niharika Bandi</a>','<a href="/profile/51"Jay Khil</a>', ''],
['<a href="/profile/64"Xiao-Lan Wong</a>','<a href="/profile/2"Patrick Cao</a>', ''],
['<a href="/profile/72"Sheldon Cheung</a>','<a href="/profile/64"Xiao-Lan Wong</a>', ''],
['<a href="/profile/81"Daniel Chen</a>','<a href="/profile/53"Jessica Wong</a>', ''],
['<a href="/profile/82"Shi Chung</a>','<a href="/profile/51"Jay Khil</a>', ''],
['<a href="/profile/92"William Ouyang</a>','<a href="/profile/53"Jessica Wong</a>', ''],
['<a href="/profile/95"Neil Sethi</a>','<a href="/profile/59"Niharika Bandi</a>', ''],
['<a href="/profile/99"Elizabeth Koh</a>','<a href="/profile/72"Sheldon Cheung</a>', ''],
['<a href="/profile/112"Christopher Jo</a>','<a href="/profile/82"Shi Chung</a>', ''],
['<a href="/profile/135"Deniz Kalaycioglu</a>','<a href="/profile/92"William Ouyang</a>', ''],
['<a href="/profile/139"Issac Kwon</a>','<a href="/profile/95"Neil Sethi</a>', ''],
['<a href="/profile/160"Vincent Liu</a>','<a href="/profile/112"Christopher Jo</a>', ''],
['<a href="/profile/168"Bernard Yuan</a>','<a href="/profile/135"Deniz Kalaycioglu</a>', ''],
['<a href="/profile/175"Adhip Sacheti</a>','<a href="/profile/81"Daniel Chen</a>', ''],
['<a href="/profile/183"Miko Bautista</a>','<a href="/profile/135"Deniz Kalaycioglu</a>', ''],
['<a href="/profile/188"Raphael Kim</a>','<a href="/profile/160"Vincent Liu</a>', ''],
['<a href="/profile/197"Olga Zubashko</a>','<a href="/profile/139"Issac Kwon</a>', ''],
['<a href="/profile/210"Tiffany Chen-Zeyu</a>','<a href="/profile/197"Olga Zubashko</a>', ''],
['<a href="/profile/216"Willa Lu</a>','<a href="/profile/183"Miko Bautista</a>', ''],
['<a href="/profile/221"Baek Kim</a>','<a href="/profile/188"Raphael Kim</a>', ''],
['<a href="/profile/234"Alex Tsai</a>','<a href="/profile/168"Bernard Yuan</a>', ''],
['<a href="/profile/247"Richard Lee</a>','<a href="/profile/197"Olga Zubashko</a>', ''],
['<a href="/profile/253"Amy Fan</a>','<a href="/profile/216"Willa Lu</a>', ''],
['<a href="/profile/259"Christine Kwon</a>','<a href="/profile/221"Baek Kim</a>', ''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('family_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        