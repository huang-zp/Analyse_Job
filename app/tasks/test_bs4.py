from bs4 import BeautifulSoup

soup = BeautifulSoup(

    """
    
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8" />
    <meta name="keywords" content="" />
    <meta http-equiv="Cache-Control" content="no-transform" />
    <meta name="description" content="上海樱蓝网络科技有限公司诚聘python3人，工作地点位于上海，薪资待遇9000-18000元/月，学历要求大专或以上，工作经验3-5年等更多招聘信息请点击查看详情【智联招聘,为您提供靠谱的人才招聘信息】" />
    <title>【python_上海樱蓝网络科技有限公司人才招聘信息】 - 智联招聘</title> 
    <meta name="mobile-agent" content="format=html5; url=https://m.zhaopin.com/jobs/CZ717862880J00096920701/" />
    <link rel="alternate" media="only screen and(max-width: 640px)" href="https://m.zhaopin.com/jobs/CZ717862880J00096920701/">
    <link type="text/css" rel="stylesheet" href="//img01.zhaopin.cn/2014/common/css/reset.css" />
    <link type="text/css" rel="stylesheet" href="//img01.zhaopin.cn/2014/rd2/css/terminalpage.css?version=20151104" />
    <link type="text/css" rel="stylesheet" href="//jobs.zhaopin.com/css/apply.css" />
    <link type="text/css" rel="stylesheet" href="//img01.zhaopin.cn/2014/rd2/css/best-plugs.css" />
    <link rel="canonical" href="http://jobs.zhaopin.com/CZ717862880J00096920701.htm" />
    <script type="text/javascript">
        var arrVarFromASP = ['', 'CZ717862880J00096920701_538_1', 'python', 'http://jobs.zhaopin.com/CZ717862880J00096920701.htm', '0001-01-02', 'y', '上海', 'http://company.zhaopin.com/CZ717862880.htm', '1'];
        var ApplyUrl = "";
        var PositionExtID = "CZ717862880J00096920701";
        var Str_CompName = "上海樱蓝网络科技有限公司";
        var tjUrl = "//my.zhaopin.com/myzhaopin/SimilarPosition.asp?pid=CZ717862880J00096920701&edu=5&ind=210500&miny=&subtype=79&cityid=538";
        var dateRefreshUrl = "//jobs.zhaopin.com/shanghai/dtref/CZ717862880J00096920701.htm";
    </script>
</head>
<body>
     <link rel="stylesheet" href="//img06.zhaopin.cn/2014/head_foot/css/head_foot.css">
 <div class="all_headcontainer">
	<div class="all_top">
		<div class="all_topcontent">
			<div class="all_topcontenter">
				<div class="all_addMod">
					<div id="companyLoginregin">
				        <a href="#" id="login_text" class="allhead_login all_common" rel="nofollow" onclick="dyweTrackEvent('newtopbarLU','clickPersonLogin')">登录</a><span class="allhead_sep"></span><a href="//passport.zhaopin.com/account/register" class="allhead_regi all_common" onclick="dyweTrackEvent('addnewlink','personregister')" rel="nofollow">注册</a>
				    </div>
					<div id="companyLogining" style="display: none;">
					    <span id="personname" title="" class="allhead_login all_common"></span><span class="allhead_sep"></span><a href="#" id="personcheckout" onclick="dyweTrackEvent('addnewlink','personexit')" class="allhead_login all_common">退出</a>
					</div>
				</div>
				<div class="all_addDiv">
					<a href="https://rd2.zhaopin.com/portal/myrd/regnew.asp?za=2&ps=1" class="allhead_postoffice all_common" target="_blank" onclick="dyweTrackEvent('addnewlink','compuser')" rel="nofollow"></a>
					<span><i class="all_icon allhead_tel"></i><b class="allhead_telcon">400-885-9898</b></span>
					<strong><a href="http://jobs.zhaopin.com/citymapsj79.html" class="allchoice_city all_common" target="_blank" onclick="dyweTrackEvent('addnewlink','choosecity')">切换城市</a></strong>
					<i class="all_icon allhead_phone"></i><a href="//img00.zhaopin.cn/2012/other/mobile/mobile.html" class="allhead_phonecon all_common" target="_blank" onclick="dyweTrackEvent('addnewlink','mobilejob')" rel="nofollow">手机求职</a>
				</div>				
			</div>
		</div>
	</div><!-- top结束 -->
	<div class="all_nav">
		<div class="all_navcontent">
			<a href="http://www.zhaopin.com/" class="allhead_img" title="智联招聘">
				<img src="//img01.zhaopin.cn/2014/head_foot/img/Allhead_logo.png" alt="智联招聘">
			</a>
			<ul class="all_navlist">
				<li><a href="http://www.zhaopin.com/">首页</a></li>
				<li><a href="http://my.zhaopin.com/">简历中心</a></li>
				<li><a href="http://sou.zhaopin.com/">职位搜索</a></li>
				<li><a href="http://xiaoyuan.zhaopin.com/" target="_blank">校园招聘</a></li>
				<li><a href="http://www.highpin.cn/zhiwei/?fromType=12&amp;utm_source=zpsygdad&amp;utm_medium=cpc&amp;utm_content=zpsygdadtextlink&amp;utm_campaign=zpsygdadanalytics&amp;utm_term=onlinepromo_201402">高端招聘</a></li>
				<li><a href="http://edu.zhaopin.com/" target="_blank" onclick="dyweTrackEvent('addnewlink','educchannal')">智联教育</a></li>
				<li><a href="http://www.zhaopin.com/jobseeker/index_industry.html" target="_blank">行业求职</a></li>
				<li><a href="http://article.zhaopin.com/">求职指导</a></li>
				<li><a href="http://ceping.zhaopin.com/" target="_blank" rel="nofollow">智联测评</a></li>
			</ul>
		</div>
	</div><!-- nav结束 -->
 </div>
<script type="text/javascript" src="//img08.zhaopin.cn/2014/head_foot/js/head_foot.js"></script>
    <div class="announcement">
        <div class="announcement-icon">智联提示您：用人单位以任何名义向应聘者收取费用都属违法行为（如押金、资料费、代收体检费、代收淘宝信誉等），请提高警惕并注意保护个人信息！</div>
    </div>
    <div class="clearfix"></div>
    <div class="bread_crumbs">
        <span>您当前所在位置</span><a href="//jobs.zhaopin.com" target="_blank"><strong>首页</strong></a>&gt;<a href="http://jobs.zhaopin.com/shanghai/" target="_blank"><strong>上海人才网</strong></a>&gt;<a href="http://jobs.zhaopin.com/shanghai/sj079/" target="_blank"><strong>上海软件研发工程师招聘</strong></a>&gt;<span>当前页面</span>
    </div>
    <!--20140610liuhuili-->
    <div class="top-fixed-box">
        <div class="fixed-inner-box">
            <div class="inner-left fl">
                <h1>python</h1>
                <h2><a onclick="recordOutboundLink(this, 'terminalpage', 'tocompanylink3');" href="http://company.zhaopin.com/CZ717862880.htm" target="_blank">上海樱蓝网络科技有限公司 <img class="icon_vip" src="//img03.zhaopin.cn/IHRNB/img/detailviph.png" border="0" vinfo="%7b%22endtime%22%3a1549295999000%2c%22limitcount%22%3a100%2c%22orgid%22%3a71786288%2c%22rdorgid%22%3a55257998%2c%22staffid%22%3a0%2c%22starttime%22%3a1506735597079%2c%22total%22%3a100%2c%22type%22%3a1002%2c%22userid%22%3a1%2c%22vipName%22%3a%22%e7%99%bd%e9%93%b6%e4%bc%9a%e5%91%98%22%7d"/></a></h2>
                <div style="width:683px;" class="welfare-tab-box"> <span>员工旅游</span><span>五险一金</span><span>股票期权</span><span>弹性工作</span><span>年终分红</span> </div>
                <div class="lightspot"></div>
            </div>
            <div class="inner-right fr">
                
                <button style="display:none;" class="now-apply" onclick="zlzp.searchjob.ajaxApplyBrig3('1');dyweTrackEvent('bjobsdetail14gb','directapply_top_right');" id="applyVacButton2" title="申请职位"></button>
                
            </div>
        </div>
    </div>
    <div class="terminalpage clearfix">
        <div class="terminalpage-left">
            <ul class="terminal-ul clearfix">
                <li><span>职位月薪：</span><strong>9000-18000元/月&nbsp;<a href="http://www.zhaopin.com/gz_shanghai/" target="_blank" title="上海工资计算器"><img src="http://jobs.zhaopin.com/images/calculator.png" alt="上海工资计算器" /></a></strong></li>
                <li><span>工作地点：</span><strong><a target="_blank" href="http://www.zhaopin.com/shanghai/">上海</a></strong></li>
                <li><span>发布日期：</span><strong><span id="span4freshdate">2018-03-12 19:35:03</span></strong></li>
                <li><span>工作性质：</span><strong>全职</strong></li>
                <li><span>工作经验：</span><strong>3-5年</strong></li>
                <li><span>最低学历：</span><strong>大专</strong></li>
                <li><span>招聘人数：</span><strong>3人 </strong></li>
                <li><span>职位类别：</span><strong><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj079/">软件研发工程师</a></strong></li>
            </ul>
            <div class="terminalpage-main clearfix">
                <ul class="tab-ul">
                    <li class="current">职位描述</li>
                    <li>公司介绍</li>
                </ul>
                <p class="collect fr"><a href="javascript:void(0)" class="reportBtn" id="reportBtn"><font></font>举报</a><a href="javascript:void(0)" rel="nofollow" onclick="zlapply.searchjob.saveJobTerminalApply(); dyweTrackEvent('bjobsdetail14gb', 'jobcollection'); return false;"><i></i>收藏</a></p>
                <div class="tab-cont-box">
                    <div class="tab-inner-cont">
                        <!-- SWSStringCutStart -->
                        <p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica="">后台Python</span><span style="font-size: 17px; font-family: 宋体;">岗位职责</span><span style="font-size: 17px; font-family: " helvetica="">:</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">负责网站后台产品的研发</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">根据需求进行方案设计和技术文档的编写</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: 宋体;">任职要求</span><span style="font-size: 17px; font-family: " helvetica="">:</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">熟悉</span><span style="font-size: 17px; font-family: " helvetica=""> Linux </span><span style="font-size: 17px; font-family: 宋体;">系统</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">熟悉</span><span style="font-size: 17px; font-family: " helvetica=""> Git </span><span style="font-size: 17px; font-family: 宋体;">等代码管理工具</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">拥有</span><span style="font-size: 17px; font-family: " helvetica=""> Python </span><span style="font-size: 17px; font-family: 宋体;">开发经验，</span><span style="font-size: 17px; font-family: " helvetica="">Flask / Django </span><span style="font-size: 17px; font-family: 宋体;">至少精通一种</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">熟悉</span><span style="font-size: 17px; font-family: " helvetica=""> RabbitMQ / Celery </span><span style="font-size: 17px; font-family: 宋体;">者优先</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">熟悉</span><span style="font-size: 17px; font-family: " helvetica=""> MongoDB / Redis / ElasticSearch </span><span style="font-size: 17px; font-family: 宋体;">者优先</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">了解分布式系统的架构和原理，有分布式系统开发经验者优先</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">有自主学习能力，良好的团队沟通能力</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><span style="font-size: 17px; font-family: " helvetica=""></span><span style="font-size: 17px; font-family: 宋体;">有维护技术博客优先</span></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">3到5年经验，有过丰富项目经验的可以适当放宽标准，不论如何，还是再强调一遍，独挡一面！<br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">员工福利：</p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">五险一金，包吃包住，年终分红奖金。</p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">因为公司主营业务是出境服务，所以公司可以很便利的为大家提供每年一次出国旅行的福利。</p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">公司氛围良好，均是朝气蓬勃的年轻人，最年长者也是85后，大多90后，希望能与同样朝气蓬勃的你一起愉快的工作。</p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);">公司设有期权池，表现优秀者均可获得公司股份。</p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><p style="font-family: simsun; margin-top: 0px; margin-bottom: 0px; padding: 0px; border: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: 25px; color: rgb(51, 51, 51); white-space: normal; background-color: rgb(255, 255, 255);"><br/></p><h1 microsoft="" margin:="" 12px="" 0px="" padding:="" border:="" font-size:="" color:="" white-space:="" background-color:="" style="font-family: simsun, ">工作地址</h1><h2 microsoft="" margin:="" padding:="" border:="" font-size:="" font-weight:="" color:="" white-space:="" background-color:="" style="font-family: simsun, ">上海市闵行区放鹤路1088号</h2><p><br/></p>
                        <!-- SWSStringCutEnd -->
                        
                        <b>工作地址：</b>
                        <h2>
                            上海市闵行区放鹤路1088号第7幢A301室
                            
                            <a href="javascript:fnOpenMiniMap('','','上海','31.047684','121.454344');" onclick="dyweTrackEvent('bjobsdetail14gb', 'showjobmap');" class="see-map">查看职位地图</a>
                            
                        </h2>
                        
                        
                        <p>
                            <button id="applyVacButton1" class="button-small" title="申请职位" onclick="zlzp.searchjob.ajaxApplyBrig3('1');dyweTrackEvent('bjobsdetail14gb','directapply_middle');"></button>
                        </p>
                        
                    </div>
                    <div class="tab-inner-cont" style="display:none;word-wrap:break-word;">
                        
                        <h5><a rel="nofollow" href="http://company.zhaopin.com/CZ717862880.htm" onclick="recordOutboundLink(this, 'terminalpage', 'tocompanylink4');" target="_blank">上海樱蓝网络科技有限公司 <img class="icon_vip" src="//img03.zhaopin.cn/IHRNB/img/detailviph.png" border="0" vinfo="%7b%22endtime%22%3a1549295999000%2c%22limitcount%22%3a100%2c%22orgid%22%3a71786288%2c%22rdorgid%22%3a55257998%2c%22staffid%22%3a0%2c%22starttime%22%3a1506735597079%2c%22total%22%3a100%2c%22type%22%3a1002%2c%22userid%22%3a1%2c%22vipName%22%3a%22%e7%99%bd%e9%93%b6%e4%bc%9a%e5%91%98%22%7d"/></a><a target="_blank" class="color-blue fr see-other-job" href="http://company.zhaopin.com/CZ717862880.htm" rel="nofollow" onclick="recordOutboundLink(this, 'terminalpage', 'tocompanylink2');">该公司其他职位</a></h5>
                        <p>
                            <p>以青岛的海淘贸易公司以及日本的旅游公司为基础，在上海组建的互联网电子商务总公司。</p><p>公司主营业务也以出境旅游及海淘为主要组成部分。</p><p>公司组成人员，总部人员由留学各国的海归人员为主要成员，日本分公司，以及正在筹备的韩国以及台湾，泰国，英国分公司成员均为当地的华人华侨以及少量所在地外国人。</p><p>诚邀四海有识之士一起团结奋斗，创造公司和个人的美好明天。</p>
                        </p>
                        

                        
                        <h3></h3>
                        <p>
                            
                        </p>

                    </div>
                </div>
            </div>
            
            <div class="today_recommend">
                <ul class="tab-ul">
                    <li class="current">职位推荐</li>
                    <li>今日相似推荐</li>
                </ul>
            </div>
            <div class="tab-cont-box">
                <div class="tab-inner-cont" style="display: block;">
                    <!--职位推荐-->
                    <div class="similar-job" id="job-zxzwtj">
                        <form name="myform" method="post" id="myform2" action="">
                            <div class="applay-All dlapplay-all applay-All-b">
                                <label><input type="checkbox" name="allvacancyid" onclick="ChkSelectAll('vacancyid', 'allvacancyid', this)" checked="" id="allvacancyid">全选</label><button onclick="return CheckApply(event);" class="selectall-btn" type="button"></button>
                            </div>
                            <ul class="batch_ul">
                                <li><p class="pone"><input checked="" name="vacancyid" value="CC219390019J00038285502_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/CC219390019J00038285502.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/CC219390019J00038285502.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title=".Net高级软件工程师">.Net高级软件工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC219390019.htm" class="company-name" target="_blank" title="上海仁库软件科技有限公司">上海仁库软件科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC219390019J00038285502_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC120085094J90250143000_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/120085094250143.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/120085094250143.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="上位机软件工程师">上位机软件工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/%E4%B8%8A%E6%B5%B7%E6%96%B0%E6%BC%AB%E4%BC%A0%E6%84%9F%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6%E5%8F%91%E5%B1%95%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_CC120085094.htm" class="company-name" target="_blank" title="上海新漫传感技术研究发展有限公司">上海新漫传感技术研究发展有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC120085094J90250143000_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC534843183J90250006000_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/534843183250006.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/534843183250006.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="PHP">PHP</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC534843183.htm" class="company-name" target="_blank" title="盐城网电科技有限公司">盐城网电科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC534843183J90250006000_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC335972313J90250006000_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/335972313250006.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/335972313250006.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title=".NET C#软件工程师">.NET C#软件工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ335972310.htm" class="company-name" target="_blank" title="上海皓为商务咨询有限公司">上海皓为商务咨询有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC335972313J90250006000_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC131688750J00026110415_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/CC131688750J00026110415.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/CC131688750J00026110415.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="视频应用软件开发工程师">视频应用软件开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ131688750.htm" class="company-name" target="_blank" title="北京创先泰克科技有限公司">北京创先泰克科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC131688750J00026110415_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC131688750J00026075015_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/CC131688750J00026075015.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/CC131688750J00026075015.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="软件开发工程师">软件开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ131688750.htm" class="company-name" target="_blank" title="北京创先泰克科技有限公司">北京创先泰克科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC131688750J00026075015_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC376727185J90250000000_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/376727185250000.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/376727185250000.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="JAVA软件开发工程师">JAVA软件开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC376727185.htm" class="company-name" target="_blank" title="上海奇云通讯科技有限公司">上海奇云通讯科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC376727185J90250000000_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC402792820J90250182000_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/402792820250182.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/402792820250182.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="系统软件开发工程师">系统软件开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ402792820.htm" class="company-name" target="_blank" title="上海鲁交测控科技有限公司">上海鲁交测控科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC402792820J90250182000_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC676193322J00061673905_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/CC676193322J00061673905.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/CC676193322J00061673905.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="C++软件工程师">C++软件工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC676193322.htm" class="company-name" target="_blank" title="上海苍枫教学设备有限公司">上海苍枫教学设备有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC676193322J00061673905_538_1_100_300__2_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CZ566509820J00051343607_538_1_100_300__2_" data-apply="1" data-url="http://jobs.zhaopin.com/CZ566509820J00051343607.htm" onclick="unChkSelectAll('allvacancyid')" type="checkbox" /><a href="http://jobs.zhaopin.com/CZ566509820J00051343607.htm" par="ssidkey=y&ff=ssb&ss=201" class="job-name" target="_blank" title="java开发工程师[中级]">java开发工程师[中级]</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ566509820.htm" class="company-name" target="_blank" title="上海澄泓信息科技有限公司">上海澄泓信息科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CZ566509820J00051343607_538_1_100_300__2_')"></strong></p></li>
                            </ul>
                            <div class="applay-All dlapplay-all applay-All-b">
                                <label><input type="checkbox" onclick="ChkSelectAll('vacancyid', 'allvacancyid', this)" name="allvacancyid" checked="" id="allvacancyid">全选</label><button onclick="return CheckApply(event);" class="selectall-btn" type="button"></button>
                            </div><p class="see-more fr"><a rel="nofollow" href="//sou.zhaopin.com/jobs/searchresult.ashx?sj=79&jl=上海" target="blank" onclick="dyweTrackEvent('bjobsdetail14gb','showmoresimjobs');">查看更多职位推荐 &gt;&gt;</a></p>
                        </form>
                    </div>
                </div>
                <div class="tab-inner-cont" style="display: none">
                    <!--相似职位推荐-->
                    <div class="similar-job" id="job-xszwtj">
                        <form name="myform" method="post" id="myform1" action="">
                            <div class="applay-All dlapplay-all applay-All-b">
                                <label><input type="checkbox" name="allvacancyid" onclick="ChkSelectAll('vacancyid', 'allvacancyid', this)" checked="" id="allvacancyid">全选</label><button onclick="return CheckApply(event);" class="selectall-btn" type="button"></button>
                            </div>
                            <ul class="batch_ul">
                                <li><p class="pone"><input checked="" name="vacancyid" value="CC567369733J90250831000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/567369733250831.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python开发工程师">Python开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC567369733.htm" class="company-name" target="_blank" title="北京欣如信科技有限公司">北京欣如信科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC567369733J90250831000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC141162210J00040598406_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/CC141162210J00040598406.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="python程序员">python程序员</a></p><p class="ptwo"><a href="http://company.zhaopin.com/P2/CC1411/6221/CC141162210.htm" class="company-name" target="_blank" title="凤瑞奇软件科技（上海）有限公司">凤瑞奇软件科技（上海）有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC141162210J00040598406_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC245471585J00070564707_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/CC245471585J00070564707.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="python开发工程师（服务端）">python开发工程师（服务端）</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC245471585.htm" class="company-name" target="_blank" title="上海展卷信息科技有限公司">上海展卷信息科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC245471585J00070564707_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC493463820J90250265000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/493463820250265.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python开发工程师">Python开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/%E5%8D%9A%E7%AD%94%E4%BC%81%E4%B8%9A%E7%AE%A1%E7%90%86%E5%92%A8%E8%AF%A2%28%E4%B8%8A%E6%B5%B7%29%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_CC493463820.htm" class="company-name" target="_blank" title="博答企业管理咨询(上海)有限公司">博答企业管理咨询(上海)有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC493463820J90250265000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC197998015J90250052000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/197998015250052.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="python开发工程师">python开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/P2/CC1979/9801/CC197998015.htm" class="company-name" target="_blank" title="上海华屹数码科技有限公司">上海华屹数码科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC197998015J90250052000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC448764837J90250036000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/448764837250036.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python开发">Python开发</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC448764837.htm" class="company-name" target="_blank" title="上海梦创双杨数据科技股份有限公司">上海梦创双杨数据科技股份有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC448764837J90250036000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CZ562114530J00029797206_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/CZ562114530J00029797206.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="python开发工程师（上海）">python开发工程师（上海）</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CZ562114530.htm" class="company-name" target="_blank" title="深圳市源极光科技有限公司">深圳市源极光科技有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CZ562114530J00029797206_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC428715824J90251194000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/428715824251194.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python开发工程师">Python开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/%E5%8C%97%E4%BA%AC%E9%87%91%E8%89%B2%E5%8D%8E%E5%8B%A4%E6%95%B0%E6%8D%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_CC428715824.htm" class="company-name" target="_blank" title="北京金色华勤数据服务有限公司">北京金色华勤数据服务有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC428715824J90251194000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC538792981J90250032000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/538792981250032.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python工程师">Python工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC538792981.htm" class="company-name" target="_blank" title="上海博为峰软件技术股份有限公司长沙分公司">上海博为峰软件技术股份有限公司长沙分公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC538792981J90250032000_538_1_31_301__1_')"></strong></p></li><li><p class="pone"><input checked="" name="vacancyid" value="CC363087212J90252731000_538_1_31_301__1_" onclick="unChkSelectAll('allvacancyid')" type="checkbox"><a href="http://jobs.zhaopin.com/363087212252731.htm" par="ssidkey=y&ff=ssb&ss=301" class="job-name" target="_blank" title="Python开发工程师">Python开发工程师</a></p><p class="ptwo"><a href="http://company.zhaopin.com/CC363087212.htm" class="company-name" target="_blank" title="海银财富管理有限公司">海银财富管理有限公司</a><span class="w150">地点：上海</span></p><p class="pthree fr"><strong onclick="applyjob('CC363087212J90252731000_538_1_31_301__1_')"></strong></p></li>
                            </ul>
                            <div class="applay-All dlapplay-all applay-All-b">
                                <label><input type="checkbox" onclick="ChkSelectAll('vacancyid', 'allvacancyid', this)" name="allvacancyid" checked="" id="allvacancyid">全选</label><button onclick="return CheckApply(event);" class="selectall-btn" type="button"></button>
                            </div><p class="see-more fr"><a rel="nofollow" href="//my.zhaopin.com/myzhaopin/SimilarPosition.asp?pid=CZ717862880J00096920701&edu=5&ind=210500&miny=&subtype=79&cityid=538" target="blank" onclick="dyweTrackEvent('bjobsdetail14gb', 'showmoresimjobs');">查看更多相似职位推荐 &gt;&gt;</a></p>
                        </form>
                    </div>
                </div>
            </div>
            
        </div>
        <div class="terminalpage-right">
            <div class="company-box">
                
                <p class="company-name-t"><a rel="nofollow" href="http://company.zhaopin.com/CZ717862880.htm" target="_blank">上海樱蓝网络科技有限公司 <img class="icon_vip" src="//img03.zhaopin.cn/IHRNB/img/detailviph.png" border="0" vinfo="%7b%22endtime%22%3a1549295999000%2c%22limitcount%22%3a100%2c%22orgid%22%3a71786288%2c%22rdorgid%22%3a55257998%2c%22staffid%22%3a0%2c%22starttime%22%3a1506735597079%2c%22total%22%3a100%2c%22type%22%3a1002%2c%22userid%22%3a1%2c%22vipName%22%3a%22%e7%99%bd%e9%93%b6%e4%bc%9a%e5%91%98%22%7d"/></a></p>
                <ul class="terminal-ul clearfix terminal-company mt20">
                    <li><span>公司规模：</span><strong>20人以下</strong></li>
                    <li><span>公司性质：</span><strong>民营</strong></li>
                    
                    
                    
                    <li><span>公司行业：</span><strong><a target="_blank" href="http://jobs.zhaopin.com/shanghai/in210500/">互联网/电子商务</a></strong></li>
                    
                    <li>
                        <span>公司地址：</span><strong>
                            上海市闵行区放鹤路1088号<br>
                            
                        </strong>
                    </li>
                </ul>
                <!--是否是反馈通-->
                <input type="hidden" id="displayRegionScopeId" name="displayRegionScopeId" value="0" />
            </div>
            <div class="terminalpage-advertising">
                <ul id="job-advertising"></ul>
            </div>
        </div>
    </div>
    <div class="bottom-list clearfix">
        <div id="footerSearchBar">
            <div class="sbf"> </div>
            <form name="frmSearch_bottom" method="get" onsubmit="return zlzp.searchjob.gotoSearch_t(document.frmSearch_bottom)">
                <input type="hidden" name="page" value="" />
                <input type="hidden" name="SchJobType" value="" />
                <input type="hidden" name="subJobtype" value="" />
                <input type="hidden" name="industry" value="" />
                <input type="hidden" name="PublishDate" value="" />
                <input type="hidden" name="sortby" value="" />
                <input type="hidden" name="SearchModel" value="0" />
                <input type="hidden" name="ref" value="jobsearch" />
                <input type="hidden" name="f_kw" value="" />
                <div class="sbc">
                    <ul>
                        <li class="searchBarSelect">
                            <input type="button" id="buttonSelJobType_bottom" name="buttonSelJobType" value="选择职位" title="选择职位" onClick="dyweTrackEvent('choosepost','postsearchsetting001')"/>

                        </li>
                        <li class="searchBarSelect">
                            <input type="button" id="buttonSelIndustry_bottom" name="buttonSelIndustry" value="选择行业" title="选择行业" onClick="dyweTrackEvent('chooseindustry','postsearchsetting001')"/>

                        </li>
                        <li>
                            <div class="keyword_bottombox">
                                <input type="text" class="keyword inputTips" name="KeyWord" id="KeyWord_kw2_bottom"
                                       value="" onfocus="zlzp.clearDefTxt(this,zlzp.searchjob.k_tips);" onblur="zlzp.setDefTxt(this,zlzp.searchjob.k_tips);"
                                       maxlength="100" style="color: rgb(204, 204, 204);" />
                            </div>
                        </li>
                        <li class="searchBarSelect searchBarSelects">
                            <input type="text" class="cityInput inputTips" id="JobLocation_bottom" name="JobLocation" value="" onfocus="zlzp.clearDefTxt(this,zlzp.searchjob.c_tips);" onblur="zlzp.setDefTxt(this,zlzp.searchjob.c_tips);" style="color: rgb(204, 204, 204);" />
                            <input type="button" id="buttonSelCity_bottom" name="buttonSelCity" title="选择城市" class="cityButton" onClick="dyweTrackEvent('choosecity','postsearchsetting001')"/>
                        </li>
                        <li style="margin-right: 0px">
                            <button class="doSearch" onclick="dyweTrackEvent('searchjob', 'postsearchsetting001'); zlzp.searchjob.gotoSearch_t(document.frmSearch_bottom);"></button>
                        </li>
                    </ul>
                </div>
            </form>
            <div class="sbl"> </div>
            <div style="clear: both"> </div>
        </div>

        <div class="bottom_container">
            
            <div class="bottom_t">
                <ul>
                    <li class="posi_te">您也许对以下职位类别感兴趣:</li>
                    <li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj045/">上海软件工程师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj047/">上海数据库开发工程师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj044/">上海高级软件工程师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj5147/">上海游戏设计师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj665/">上海需求工程师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj079/">上海软件开发工程师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj5153/">上海软件界面设计招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj667/">上海系统架构设计师招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj5148/">上海手机游戏开发招聘</a></li>
<li><a target="_blank" href="http://jobs.zhaopin.com/shanghai/sj5129/">上海手机软件开发招聘</a></li>

                </ul>
            </div>
            
            
            <div class="bottom_m">
                <ul>
                    <li class="posi_hot">热门职位推荐:</li>
                    <li><a target="_blank" href="http://jobs.zhaopin.com/hot_sjcjrjkfgcs/">数据采集软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_cpqrsrjkfgcs/">产品嵌入式软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_jqsjrjkfgcs/">机器视觉软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_qrsptrjkfgcs/">嵌入式平台软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_dnbrjkfgcs/">电能表软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_ydtxrjkfgcs/">移动通信软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_tyrjkfgcs/">通讯软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_xmqrsrjkfgcs/">项目嵌入式软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_sjxyrjkfgcs/">手机协议软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_xxjsrjkfgcs/">信息技术软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_znsjyyrjkfgcs/">智能手机应用软件开发工程师招聘</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hot_ylrjkfgcs/">医疗软件开发工程师招聘</a></li>
                </ul>
            </div>
            
            
            <div class="bottom_b">
                <ul>
                    <li class="posi_rou">周边城市:</li>
                    <li><a target="_blank" href="http://jobs.zhaopin.com/suzhou/">苏州人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/wuxi/">无锡人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/jiaxing/">嘉兴人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/hangzhou/">杭州人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/changzhou/">常州人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/huzhou/">湖州人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/nanjing/">南京人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/yangzhou/">扬州人才网</a></li><li><a target="_blank" href="http://jobs.zhaopin.com/ningbo/">宁波人才网</a></li>
                </ul>
            </div>
            
        </div>
    </div>
    <div class="back-to"> </div>
    <div id="zlzp_jsc"> </div>
    <div style="clear: both;"> </div>
    <!--收藏成功弹框-->
    <div class="addpopupApply" style="width:340px;left: 750px; top: 469px; display: none; opacity: 1;">
        <div class="topBar">
            <p>收藏</p>
            <a title="关闭"><img src="//img02.zhaopin.cn/2014/common/img/icon_close_mout.gif"></a>
        </div>
        <div style="position: relative;">
            <div class="mainBlock">
                <div id="loginBlock">
                    <div id="sou-collect" class="sou-collect">
                        <div id="sou-collect-title" class="collect-title"><i></i> 收藏成功<!-- 此职位已收藏--> </div>
                        <div id="sou-collect-content" class="collect-content"> 您可以在 <a target="_blank" href="//my.zhaopin.com/myzhaopin/jobmng_fav.asp">职位收藏夹</a> 中查看 </div>
                    </div>
                    <p class="buttons"><span class="popupCancelBtn">关闭</span></p>
                </div>
            </div>
            <div class="loading" style="width: 420px; height: 129px; visibility: visible; display: none;"></div>
        </div>
    </div>
    <div class="layer-01"></div>
    <!--投递监控-->
    <input type="hidden" id="jobcode" value="1" />
    <div class="allfoot_link">
    <div class="allfoot_linkcon">
        <a onmousedown="return AdsClick(121115223, 'zhilianjieshao')" target="_blank" href="http://special.zhaopin.com/sh/2009/aboutus/about.html" rel="nofollow">智联介绍</a> | <a target="_blank" href="http://www.zhaopin.com/sitemap.html">网站地图</a> | <a onmousedown="    return AdsClick(121115223, 'jiaruzhilian')" target="_blank" href="http://special.zhaopin.com/sh/2009/aboutus/join.html" rel="nofollow">加入智联</a> | <a onmousedown="    return AdsClick(121115223, 'falvshengming')" target="_blank" href="http://special.zhaopin.com/sh/2009/aboutus/law.html" rel="nofollow">法律声明</a> | <a onmousedown="    return AdsClick(121115223, 'baomichengnuo')" target="_blank" href="http://special.zhaopin.com/sh/2009/aboutus/secrecy.html" rel="nofollow">隐私政策</a> | <a onmousedown="    return AdsClick(121115223, 'lianxifangshi')" target="_blank" href="http://special.zhaopin.com/sh/2009/aboutus/contact.html" rel="nofollow">联系方式</a> | <a onmousedown="    return AdsClick(121115223, 'changjianwenti')" target="_blank" href="http://jobseeker.zhaopin.com/zhaopin/faq/question.html" rel="nofollow">常见问题</a> | <a onmousedown="    return AdsClick(121115223, 'touzizheguanxi')" target="_blank" href="http://ir.zhaopin.com" rel="nofollow">Investor Relations</a>您对 Zhaopin.com 有任何建议或意见请<a onclick="window.open('http://img00.zhaopin.cn/2014/common/html/rdimpop.html', '_blank', 'width=702,height=702,left=100,top=60,scrollbars=0,overflow=auto,status=0');" onmousedown="    return AdsClick(121115223, 'contactus')" href="#" rel="nofollow">联系我们</a><br>未经zhaopin.com 同意，不得转载本网站之所有招聘信息及作品
        智联招聘网版权所有 ©<br>京ICP备12025925号 <a href="http://www.miibeian.gov.cn" target="_blank">京ICP证010207号</a> 电信业务审批[2001]字第233号函<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502002133" class="foot_public" rel="nofollow">京公网安备11010502002133号</a>
    </div>
</div>
    <script type="text/javascript" src="//img01.zhaopin.cn/2012/js/jquery-1.6.4.min.js"></script>
    
    
    <script type="text/javascript" src="//jobsgg.zhaopin.com/ZHAOPIN_JOB_DETAIL_RIGHT_SHANGHAI.htm" id="positionad"></script>
    
    <!-- begin 反馈通 -->
    <link href="//img01.zhaopin.cn/2014/common/css/reset-min.css" rel="stylesheet" type="text/css" />
    <link href="//img01.zhaopin.cn/2014/common/css/feedback/feedback-tip.css" rel="stylesheet" type="text/css" />
    <script src="//img01.zhaopin.cn/2014/common/js/jobapply/job-apply.js"></script>
    <script src="//img01.zhaopin.cn/2014/common/js/window.dialog.01.js"></script>
    <!-- end 反馈通 -->
    <script type="text/javascript" src="//img01.zhaopin.cn/2012/js/basedata.js"></script>
    <script type="text/javascript" src="//img02.zhaopin.cn/2012/js/jobs/terminalpage_new.js?version=20180301"></script>
    <script type="text/javascript" src="//img02.zhaopin.cn/2014/common/js/zpidc.utils.js"></script>
    <script type="text/javascript" src="//img01.zhaopin.cn/2014/common/js/zpidc.login.js"></script>
    <script type="text/javascript" src="//img01.zhaopin.cn/2014/jobs/js/ajaxapplynow.js?version=20180301"></script>
    <script type="text/javascript" src="//img02.zhaopin.cn/2012/js/sou/searchresult1.js?version=20180301"></script>
    <script type="text/javascript" src="//img01.zhaopin.cn/2014/jobs/js/best-plugs.js"></script>
    <script type="text/javascript" src="//img03.zhaopin.cn/2014/jobs/js/ga.js?version=20180301?version=20180228"></script>
    <script type="text/javascript" src="//img04.zhaopin.cn/2012/js/za/ga.js?version=20180228"></script>
    <script type="text/javascript">
        try {
            var _mvq = window._mvq || [];
            window._mvq = _mvq;
            _mvq.push(['$setAccount', 'm-196569-0']);

            _mvq.push(['$setGeneral', 'goodsdetail', '', /*用户名*/ '', /*用户id*/ '']);
            _mvq.push(['$logConversion']);

            _mvq.push(['setPageUrl', /*单品着陆页url*/ '']); //如果不需要特意指定单品着陆页url请将此语句删掉
            _mvq.push(['$addGoods', /*分类id*/ '', /*品牌id*/ '', /*商品名称*/ 'python', /*商品ID*/_getproductid(), /*商品售价*/ _getsalary(), /*00商品图片url*/ _getcomplogo(), /*分类名*/ _getindustry(), /*品牌名*/ '', /*商品库存状态1或是0*/ '', /*网络价*/ '', /*收藏人数*/ '', /*商品下架时间*/ '']);
            _mvq.push(['$addPricing', /*价格描述*/ _getsalary()]);
            _mvq.push(['$logData']);
            
            function _getsalary() {
                var s = '9000-18000元/月';
                var g = new RegExp('\\d+', 'g');
                if (g.test(s)) {
                    var t = g.exec(s);
                    var a = [];
                    while (t) {
                        a.push(Number(t[0]));
                        t = g.exec(s);
                    }
                    return a.sort(function(x, y) { return x - y; }).reverse()[0];
                } else {
                    return s;
                }
            }
			
			function _getindustry(){
			    var s = '<a target="_blank" href="http://jobs.zhaopin.com/shanghai/in210500/">互联网/电子商务</a>';
			    var g = new RegExp('<\/?a[^>]*>', 'g');
				s = s.replace(g,'');
				return s;
			}

            function _getproductid() {
                var g = new RegExp('\\d+');
                return g.exec('http://jobs.zhaopin.com/CZ717862880J00096920701.htm')[0];
            }

            function _getcomplogo() {
                var logo = '';
                if (logo.replace(/\s+/g, '').length == 0) {
                    logo = '//img01.zhaopin.cn/2014/rd2/img/default360.jpg';
                }
                return logo;
            }

        } catch (e) {
            
        }
    </script>
</body>
</html>
    
    """, 'lxml')





print(soup.find(class_="inner-left fl").h1.get_text().strip())

print(soup.find(class_="inner-left fl").h2.get_text().strip())


welfare = ''
for i in soup.find(class_="inner-left fl").div.find_all('span'):
    welfare = welfare + i.get_text().strip() + ';'
print(welfare)


for i in soup.find(class_="terminalpage-left").find(class_='terminal-ul clearfix').find_all('li'):
    print(i.strong.get_text().strip())

# for i, table in enumerate(soup.find(class_="newlist_list_content").find_all("table")):
#     if i==0:
#         continue
#     print(table.tr.td.div.a['href'])
#     print(table.tr.td.div.a.get_text().strip())

