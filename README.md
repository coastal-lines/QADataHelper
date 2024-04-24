<h2 class="code-line" data-line-start="0" data-line-end="1"><a id="QA_Data_Helper_0"></a>QA Data Helper</h2>
<h5 class="code-line" data-line-start="1" data-line-end="2"><a id="Data_Visualization_Statistics_and_Metrics_for_daily_testing_tasks_1"></a>Data Visualization, Statistics and Metrics for daily testing tasks</h5>
<h5 class="code-line" data-line-start="2" data-line-end="3"><a id="Extension_for_Broadcom_Rally_Agile_tool_2"></a>Extension for Broadcom Rally Agile tool</h5>
<h1 class="code-line" data-line-start="3" data-line-end="4"><a id="_3"></a></h1>
<p class="has-line-data" data-line-start="6" data-line-end="7"><img src="https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/main_scr.jpg?raw=true" alt="image"></p>

<h1 class="code-line" data-line-start="8" data-line-end="9"><a id="_8"></a></h1>
<h4 class="code-line" data-line-start="11" data-line-end="12"><a id="Description_11"></a>Motivation</h4>
<pre>
<code class="has-line-data" data-line-start="127" data-line-end="129" class="language-sh">Working on a complex project with highly demanding sprints, 
I decided to create a tool to streamline working with QA data.

Instead of tedious manual data collection, 
the tool allows for quickly obtaining visual statistics and other information.</code>
</pre>


<h1 class="code-line" data-line-start="8" data-line-end="9"><a id="_8"></a></h1>
<h4 class="code-line" data-line-start="11" data-line-end="12"><a id="Description_11"></a>Description</h4>
<pre>
<code class="has-line-data" data-line-start="127" data-line-end="129" class="language-sh">Generally the tool helps in planning testing, estimating tasks, optimizing the set of test cases, etc.</code>
</pre>
<pre>
<code class="has-line-data" data-line-start="127" data-line-end="129" class="language-sh">Can be especially helpful for using with Shift-Left testing approach in Agile teams</code>
</pre>
<pre>
<code class="has-line-data" data-line-start="127" data-line-end="129" class="language-sh">Also, the tool can be useful for QA Leads in distributing tasks between teams</code>
</pre>
<h1 class="code-line" data-line-start="14" data-line-end="15"><a id="_14"></a></h1>
<h4 class="code-line" data-line-start="19" data-line-end="20"><a id="Features_19"></a>Features</h4>
<ul>
<li class="has-line-data" data-line-start="20" data-line-end="23">Search capabilities
<ul>
<li class="has-line-data" data-line-start="21" data-line-end="22">Using the original search syntax from Rally Agile</li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Additional search options within Input and Expected fields</li>
</ul>
<p>
<details>
  <summary>screenshot</summary>

  ![query](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/query_scr.jpg)
</details>
</li>
<li class="has-line-data" data-line-start="23" data-line-end="26">Displaying the structure of tests
<ul>
<li class="has-line-data" data-line-start="24" data-line-end="25">View the structure of test cases as a tree instead of non-informative sheet</li>
<li class="has-line-data" data-line-start="25" data-line-end="26">Simple way to copy filtered test list into feature, test report, etc</li>
</ul>
<p>
<details>
  <summary>screenshot</summary>

  ![structures_scr](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/structures_scr.jpg)
</details>
</li>
<li class="has-line-data" data-line-start="26" data-line-end="33">Data visualization
<ul>
<li class="has-line-data" data-line-start="27" data-line-end="28">Ratio of successful test cases to unsuccessful ones</li>
<li class="has-line-data" data-line-start="28" data-line-end="29">Number of defects for each Priority</li>
<li class="has-line-data" data-line-start="29" data-line-end="30">Ratio of manual test case execution time to automated</li>
<li class="has-line-data" data-line-start="30" data-line-end="31">Number of test steps and average number of text lines in steps</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">Ratio of manual to automated test cases</li>
<li class="has-line-data" data-line-start="32" data-line-end="33">Display of the number of test cases for each type</li>
</ul>
<p>
<details>
  <summary>screenshot</summary>

  ![details_scr](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/details_scr.jpg)
</details>
</li>
<li class="has-line-data" data-line-start="33" data-line-end="36">Defect chart for a set of test cases
<ul>
<li class="has-line-data" data-line-start="34" data-line-end="35">For the entire period from the earliest defect to the latest</li>
<li class="has-line-data" data-line-start="35" data-line-end="36">For a three-month period (depending on the project’s release frequency)</li>
</ul>
<p>
<details>
  <summary>screenshot</summary>

  ![timeline_scr](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/timeline_scr.jpg)
</details>
</li>
<li class="has-line-data" data-line-start="36" data-line-end="39">Advanced search and visualization of statistics for selective parameters
<ul>
<li class="has-line-data" data-line-start="37" data-line-end="38">Ratio of selective test cases to the total number of cases</li>
<li class="has-line-data" data-line-start="38" data-line-end="39">Output of brief statistics for each selective set</li>
</ul>
<p>
<details>
  <summary>screenshot</summary>

  ![ext_details_scr](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/ext_details_scr.jpg)
</details>
</li>
<li class="has-line-data" data-line-start="39" data-line-end="41">The ability to work with data in offline</li>
</ul>
<h1 class="code-line" data-line-start="41" data-line-end="42"><a id="_41"></a></h1>
<h4 class="code-line" data-line-start="43" data-line-end="44"><a id="Used_python_version_43"></a>Used python version</h4>
<ul>
<li class="has-line-data" data-line-start="44" data-line-end="46">3.12.2</li>
</ul>
<h1 class="code-line" data-line-start="46" data-line-end="47"><a id="_46"></a></h1>
<h4 class="code-line" data-line-start="48" data-line-end="49"><a id="Installation_cmd_48"></a>Installation (cmd)</h4>
<ul>
<li class="has-line-data" data-line-start="49" data-line-end="50">Please check your python version</li>
</ul>
<pre><code class="has-line-data" data-line-start="51" data-line-end="53" class="language-sh">python --version
</code></pre>
<ul>
<li class="has-line-data" data-line-start="53" data-line-end="54">Clone this project into your machine</li>
</ul>
<pre><code class="has-line-data" data-line-start="55" data-line-end="59" class="language-sh"><span class="hljs-built_in">cd</span> &lt;your_projects_folder&gt;
git <span class="hljs-built_in">clone</span> https://github.com/coastal-lines/QADataHelper.git
<span class="hljs-built_in">cd</span> QADataHelper
</code></pre>
<ul>
<li class="has-line-data" data-line-start="59" data-line-end="60">Create virtual environment and activate it</li>
</ul>
<pre><code class="has-line-data" data-line-start="61" data-line-end="64" class="language-sh">python -m venv venv
venv\Scripts\activate
</code></pre>
<ul>
<li class="has-line-data" data-line-start="64" data-line-end="65">Install requirements</li>
</ul>
<pre><code class="has-line-data" data-line-start="66" data-line-end="68" class="language-sh">pip install -r requirements.txt
</code></pre>
<ul>
<li class="has-line-data" data-line-start="68" data-line-end="69">Please check that <a href="https://tkdocs.com/tutorial/install.html#installwin">Tkinter</a> library is included in the default python installation</li>
</ul>
<pre><code class="has-line-data" data-line-start="70" data-line-end="74" class="language-sh">python
&gt;&gt;&gt; import tkinter
&gt;&gt;&gt; tkinter._<span class="hljs-built_in">test</span>()
</code></pre>
<h1 class="code-line" data-line-start="75" data-line-end="76"><a id="_75"></a></h1>
<h4 class="code-line" data-line-start="77" data-line-end="78"><a id="How_to_run_application_cmd_77"></a>How to run application (cmd)</h4>
<pre><code class="has-line-data" data-line-start="79" data-line-end="83" class="language-sh"><span class="hljs-built_in">cd</span> &lt;QADataHelper_folder&gt;
venv\Scripts\activate
main.py
</code></pre>
<h4 class="code-line" data-line-start="84" data-line-end="85"><a id="How_to_run_application_without_service_access_cmd_84"></a>How to run application without service access (cmd)</h4>
<pre><code class="has-line-data" data-line-start="86" data-line-end="90" class="language-sh"><span class="hljs-built_in">cd</span> &lt;QADataHelper_folder&gt;
venv\Scripts\activate
main.py -viewmode demo
</code></pre>
<h1 class="code-line" data-line-start="91" data-line-end="92"><a id="_91"></a></h1>
<h4 class="code-line" data-line-start="93" data-line-end="94"><a id="Some_of_scenarios_for_using_93"></a>Some of scenarios for using</h4>
<pre><code class="has-line-data" data-line-start="95" data-line-end="97" class="language-sh">Real-time server interactions
</code></pre>
<ul>
<li class="has-line-data" data-line-start="97" data-line-end="100">Connect to the server:
<ul>
<li class="has-line-data" data-line-start="98" data-line-end="99">Enter all credentials</li>
<li class="has-line-data" data-line-start="99" data-line-end="100">Click ‘Start session’</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="100" data-line-end="101"><a id="_100"></a></h1>
<ul>
<li class="has-line-data" data-line-start="101" data-line-end="104">Get test cases by query
<ul>
<li class="has-line-data" data-line-start="102" data-line-end="103">Connect to the server</li>
<li class="has-line-data" data-line-start="103" data-line-end="104">Click ‘Find’</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="104" data-line-end="105"><a id="_104"></a></h1>
<ul>
<li class="has-line-data" data-line-start="105" data-line-end="108">Get test cases by extended query
<ul>
<li class="has-line-data" data-line-start="106" data-line-end="107">Get test cases by query</li>
<li class="has-line-data" data-line-start="107" data-line-end="108">Click ‘Extended search’</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="108" data-line-end="109"><a id="_108"></a></h1>
<ul>
<li class="has-line-data" data-line-start="109" data-line-end="114">Download test cases from the root folder
<ul>
<li class="has-line-data" data-line-start="110" data-line-end="111">Connect to the server</li>
<li class="has-line-data" data-line-start="111" data-line-end="112">Click ‘Download data from the root folder’</li>
<li class="has-line-data" data-line-start="112" data-line-end="113">Wait until all requests will be finished</li>
<li class="has-line-data" data-line-start="113" data-line-end="114">Save serialized data into file</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="114" data-line-end="115"><a id="_114"></a></h1>
<ul>
<li class="has-line-data" data-line-start="115" data-line-end="120">Download test cases by default filtering
<ul>
<li class="has-line-data" data-line-start="116" data-line-end="117">Connect to the server</li>
<li class="has-line-data" data-line-start="117" data-line-end="118">Get test cases by query</li>
<li class="has-line-data" data-line-start="118" data-line-end="119">Click ‘Save’ button</li>
<li class="has-line-data" data-line-start="119" data-line-end="120">Save serialized data into file</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="120" data-line-end="121"><a id="_120"></a></h1>
<ul>
<li class="has-line-data" data-line-start="121" data-line-end="125">Download test cases by extended filtering
<ul>
<li class="has-line-data" data-line-start="122" data-line-end="123">Get test cases by extended query</li>
<li class="has-line-data" data-line-start="123" data-line-end="124">Click ‘Save’ button</li>
<li class="has-line-data" data-line-start="124" data-line-end="125">Save serialized data into file</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="125" data-line-end="126"><a id="_125"></a></h1>
<pre><code class="has-line-data" data-line-start="127" data-line-end="129" class="language-sh">Offline interactions
</code></pre>
<ul>
<li class="has-line-data" data-line-start="129" data-line-end="133">Work in demo mode
<ul>
<li class="has-line-data" data-line-start="130" data-line-end="131">Сlick ‘Upload data’</li>
<li class="has-line-data" data-line-start="131" data-line-end="132">Select ‘&lt;QADataHelper_folder&gt;\resources\data\synthetic_testcases_data.data’</li>
<li class="has-line-data" data-line-start="132" data-line-end="133">Continue work with Extended Filtering</li>
</ul>
</li>
</ul>
<h1 class="code-line" data-line-start="133" data-line-end="134"><a id="_133"></a></h1>
<ul>
<li class="has-line-data" data-line-start="134" data-line-end="138">Load previously saved test cases for offline mode working
<ul>
<li class="has-line-data" data-line-start="135" data-line-end="136">Сlick ‘Upload data’</li>
<li class="has-line-data" data-line-start="136" data-line-end="138">Continue work with Extended Filtering</li>
</ul>
</li>
</ul>