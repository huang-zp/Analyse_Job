Highcharts.chart('morris-area-chart', {

    title: {
        text: '六大职业近七天平均工资折线图'
    },

    subtitle: {
        text: 'Source: AJ平台'
    },
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
        },
    yAxis: {
        title: {
            text: '平均工资（元）'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
        pointStart: Date.UTC(2018, 3, 21),
        pointInterval: 24 * 3600 * 1000 // one day
        }
    },

    series: [{
        name: 'Python',
        data: data
    }, {
        name: 'Java',
        data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        name: 'C++',
        data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        name: 'C',
        data: [5642, 5453, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        name: 'PHP',
        data: [2908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }, {
        name: 'C#',
        data: [3332, 5354, 3334, 4323, 4443, 2224, 6665, 8888]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});

Highcharts.chart('morris-bar-chart', {
    chart: {
        type: 'column'
    },
    title: {
        text: ' 九大职业近三天岗位柱状图'
    },
    subtitle: {
        text: 'Source: AJ平台'
    },
    xAxis: {
        categories: [
            'Python',
            'Java',
            'C++',
            'C',
            'PHP',
            'C#',
            'Android',
            'iOS',
            'HTML5'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: '职位数 (个)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
        name: '2018.03.25',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 194.1, 95.6, 54.4]

    }, {
        name: '2018.03.26',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 106.6, 92.3]

    }, {
        name: '2018.03.27',
        data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 65.2, 59.3, 51.2]

    }]
});

Highcharts.chart('morris-donut-chart', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: '六大职业职位占比饼形图'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                style: {
                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                }
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Python',
            y: 26.33
        }, {
            name: 'Java',
            y: 24.03
        }, {
            name: 'C++',
            y: 20.38,
            sliced: true,
            selected: true
        }, {
            name: 'C',
            y: 14.77
        }, {
            name: 'PHP',
            y: 5.91
        }, {
            name: 'C#',
            y: 5.2
        }]
    }]
});
