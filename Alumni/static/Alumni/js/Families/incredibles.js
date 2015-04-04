function Incredibles() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Samiah Akhtar','',''],
['Arish Gupta','',''],
['Rona Song','',''],
['Wei-Wei Wang','',''],
['Brian Loo','Arish Gupta',''],
['Linda Min','Brian Loo',''],
['Salman Khoja','Salman Khoja',''],
['Eric Tang-2','Wei-Wei Wang',''],
['Alex Voo','Salman Khoja',''],
['Steven Yi','Linda Min',''],
['Joon Yoon','Eric Tang-2',''],
['David Leong','David Leong',''],
['Elizabeth Mutisya','Brian Loo',''],
['Andrew Yi','Linda Min',''],
['Billy Litner','Brian Loo',''],
['Bin Yang','Salman Khoja',''],
['Kent Yeung','David Leong',''],
['Victoria Docherty','David Leong',''],
['Hyejoo Kim','Kent Yeung',''],
['Yeonjoo Kim','Steven Yi',''],
['Stephanie Schneider','Billy Litner',''],
['Gina Seguiti','Bin Yang',''],
['Yinglu Yao','Victoria Docherty',''],
['Joy Kang','Victoria Docherty',''],
['Vince Ye','Andrew Yi',''],
['Arthur Hong','Billy Litner',''],
['Phil Chen','Yinglu Yao',''],
['Elise Lim','Stephanie Schneider',''],
['Dorothy Yu','Yeonjoo Kim',''],
['Christine Pak','Hyejoo Kim',''],
['Peter Salim','Joy Kang',''],
['Mia Wang','Vince Ye',''],
['Shanna Chan','Joy Kang',''],
['Andrew Gumbs','Mia Wang',''],
['Michael Loffredo','Arthur Hong',''],
['Manuel Garber','Dorothy Yu',''],
['Jonathan Xianqi-Zeng','Christine Pak',''],
['Ashley Wong','Peter Salim',''],
['Qifang Cai','Phil Chen',''],
['Cosette Esnes','Manuel Garber',''],
['Tiffany Fu','Manuel Garber',''],
['Abhishek Yadav','Julia Choicer',''],
['Shashank Goyal','Manuel Garber',''],
['Shannon Lin','Michael Loffredo',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('incredibles_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        