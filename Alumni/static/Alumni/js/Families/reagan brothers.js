
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Brian Ju'',''],'
['Anuj Kumar'',''],'
['Abhishek Shah'',''],'
['Kenneth Sim'',''],'
['Peter Sukits'',''],'
['Jigar Vora'',''],'
['Malvika Tamhane'',''Malvika Tamhane'' ',' ',],
['Matthew Tsau'',''Matthew Tsau'' ',' ',],
['Nicholas Yoder'',''Nicholas Yoder'' ',' ',],
['Raymond Liu'',''Raymond Liu'' ',' ',],
['Matt Glantz'',''Matt Glantz'' ',' ',],
['Mark Luk'',''Mark Luk'' ',' ',],
['Victor Tam'',''Victor Tam'' ',' ',],
['William Chu'',''William Chu'' ',' ',],
['Wangeci Ngari'',''Wangeci Ngari'' ',' ',],
['Valerie Jordan'',''Valerie Jordan'' ',' ',],
['Seungtaek Park'',''Seungtaek Park'' ',' ',],
['Shing Yan'',''],'
['Suraj Baxi'',''Suraj Baxi'' ',' ',],
['Alisa Deychman'',''Alisa Deychman'' ',' ',],
['Sean Kim'',''Sean Kim'' ',' ',],
['Nicole Tseng'',''],'
['Daria Wong'',''Daria Wong'' ',' ',],
['Jun Lee'',''],'
['Elsa Wu'',''Elsa Wu'' ',' ',],
['Tricia Chiou'',''],'
['Brian Groudan'',''Brian Groudan'' ',' ',],
['Andrew Yeung'',''Andrew Yeung'' ',' ',],
['Kathryn Davis'',''Kathryn Davis'' ',' ',],
['Amanda Ho'',''Amanda Ho'' ',' ',],
['Stefanie Chan'',''Stefanie Chan'' ',' ',],
['Megan Kwan'',''Megan Kwan'' ',' ',],
['David Baboolall'',''David Baboolall'' ',' ',],
['Kathleen Dolan'',''Kathleen Dolan'' ',' ',],
['Vivek Sainanee'',''Vivek Sainanee'' ',' ',],
['Heidi Yang'',''],'
['Lincoln He'',''Lincoln He'' ',' ',],
['Margo Johnson'',''Margo Johnson'' ',' ',],
['Barnik Saha'',''Barnik Saha'' ',' ',],
['Justin Lechner'',''],'

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    