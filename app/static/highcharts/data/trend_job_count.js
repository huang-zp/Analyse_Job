Highcharts.chart('trend-job-count-Python', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Java', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-C++', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-PHP', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-数据挖掘', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-搜索算法', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-精准推荐', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-C', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-C#', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-全栈工程师', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-.NET', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Hadoop', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Delphi', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-VB', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Perl', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Ruby', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Node.js', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Go', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-ASP', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Shell', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-后端开发其它', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-HTML5', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Android', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-iOS', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-WP', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-移动开发其它', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-web前端', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-Flash', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-html5', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});
Highcharts.chart('trend-job-count-JavaScript', {
    chart: {
        type: 'area',
        height: 200,
        width:500
    },
    title: {
        text: null
    },
    colors: ['#0d233a', '#0d233a', '#8bbc21', '#910000', '#1aadce',
       '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
    xAxis: {
        type: 'datetime',
        maxZoom: 48 * 3600 * 1000
    },
    yAxis: {
        title: {
            text: '职位数量（个）'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {

            pointStart: Date.UTC(2018, 3, 25),
            pointInterval: 24 * 3600 * 1000, // one day
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'Python',
        data: [200, 184, 199, 231, 157, 231, 190]
    }]
});

