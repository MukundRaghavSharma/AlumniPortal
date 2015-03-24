   <script>
   google.load("visualization", "1", {packages:["orgchart"]});
          google.setOnLoadCallback(drawChart);
          function drawChart() {
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'Manager');
            data.addColumn('string', 'ToolTip');

            data.addRows([
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Daniel Kim', '', '<div class="profile-box"></div>'],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Imee Chan', '', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Melanie Mu', '', ''],
              // [{v:'Jim', f:'Jim<div style="color:red; font-style:italic">Vice President<div>'}, 'Mike', 'VP'],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Lu Zhang', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Melanie Mu', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Konstantin Vidensky', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Lu Zhang', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Zachary Rousselle', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Konstantin Vidensky', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Nathaniel Eliason', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Zachary Rousselle', ''],
              // ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/> Zachary Rousselle', 'Konstantin Vidensky', ''],
              // ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Nathaniel Eliason', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Zachary Rousselle', ''],
              // ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Nathaniel Benzaquen', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Zachary Rousselle', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Alvin Mathew', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Nathaniel Eliason', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Shreeyagya Khemka', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Nathaniel Eliason', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Ellen Lai', '', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Anna Ly', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Ellen Lai', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Jason Ma', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Anna Ly', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Scarlett Su', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Anna Ly', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Alvin Poh', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Scarlett Su', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Hugo Zhang', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Jason Ma', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Ahmad Shamsuddin', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Hugo Zhang', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Dixon Liang', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Ahmad Shamsuddin', ''],
              ['<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Yvonne Yuan Jiayin', '<img src="http://127.0.0.1:8000/Alumni/media/404.jpg" class="pull-left" width=20/>Dixon Liang', ''],

            ]);

            var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
            chart.draw(data, {allowHtml:true, nodeClass:"node"});
          }
       </script>