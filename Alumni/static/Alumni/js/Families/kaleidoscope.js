
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Deneka Hypolite'',''],'
['Ellen Lai'',''],'
['Chris Lee'',''],'
['Jessica Ma'',''],'
['Nabila Walji'',''],'
['Ran Yi'',''],'
['Randall Aluwi'',''],'
['Eric Tang'',''],'
['Chris Chan'',''Chris Chan'' ',' ',],
['Christine Chang'',''Christine Chang'' ',' ',],
['Margaret Sheng'',''],'
['Amanda Davenport'',''Amanda Davenport'' ',' ',],
['Song Im'',''Song Im'' ',' ',],
['Parthesh Karna'',''Parthesh Karna'' ',' ',],
['Casey Piper'',''Casey Piper'' ',' ',],
['Min Kim'',''Min Kim'' ',' ',],
['Michelle Berman'',''Michelle Berman'' ',' ',],
['Umang Patel'',''Umang Patel'' ',' ',],
['Kunal Natu'',''],'
['Lydia Yi'',''Lydia Yi'' ',' ',],
['Alvi Hasan'',''Alvi Hasan'' ',' ',],
['Sidharth Madan'',''Sidharth Madan'' ',' ',],
['Jisoo Park'',''Jisoo Park'' ',' ',],
['Carol Kim'',''Carol Kim'' ',' ',],

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    