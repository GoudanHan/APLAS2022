<h1 id="header"> APLAS2022 </h1>

<h1 id="intro"> Artifacts </h1>
<!-- <h2> Paper Abstract </h2>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the <a href="https://arxiv.org/pdf/1708.07583.pdf">state-of-the-art NATE</a>'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p> -->
<ul>
  <li><a href="#training">Kaggle Notebooks </a>
    <ol>
      <li><a href="#models">Our machine learning models</a></li>
      <li><a href="https://www.kaggle.com/datasets/allengeng123/ocamlerrordata">NATE's dataset, SP14 and FA15</a></li>
      <li><a href="https://huggingface.co/datasets/AllenGeng/ocamlnoviceddata"><em>Dataset</em>: 20k OCaml programs written by beginners</a></li>
      <li><a href="https://huggingface.co/datasets/AllenGeng/ocamlgithub"><em>Dataset</em>: 350k OCaml programs from GitHub</a></li>
    </ol>
  </li>
  <li><a href="#nate">Our Virtual Machine</a>
    <ol>
      <li>NATE's models under the new metric</li>
      <li>Scripts and commands to get models' blame/diagnosis accuracy</li> 
    </ol>
  </li>
  <li><a href="#graph">Scripts for Generating Graphs</a></li>
</ul>
<p>Since the datasets and Kaggle notebooks are stored online, and the virtual machine is public to anyone on Dropbox. The our artifact submitted on Zenodo will just be the scripts for generating the graphs, which contain size less than 1M.</p>
<h2> Experiments </h2>
<p>Recall the two main experiments we've done in this work.</p>
<ul>
  <li><a href="#training">Natural Language models' accuracies.</a></li>
  <li><a href="#nate">Redo NATE's experiment under the <em>new metric</em>.</a></li>
</ul>

<h2 id="training">Natrual language models' accruacies </h2>
<h3>Environment Introduction & Setting up </h3>
There are two ways to reproduce this line of experiments:
  <ul>
  <li>Run virtually on Kaggle notebook with its GPU accelerator</li>
  <li>Run locally with Jupyter notebooks</li>
  </ul>
  
  
<h3 id ="models" > Calculate models' accruacies </h3>  
Run <a href="https://www.kaggle.com/code/tianyuhan2/inference-7fa4ae/edit"> Inference notebook.</a> 
The notebook requires two input: model and task, which you need to select from the following table. And it currently support the following calculations:

<table align="center">
  <tr>
    <th></th>
    <th>SP14->FA15</th>
    <th>FA15->SP14</th>
 </tr>
 <tr>
    <th>BERT Small</th>
    <th>model = "bert-small"; task="14to15"</th>
    <th>model = "bert-small"; task="15to14"</th>
 </tr>
 <tr>
    <th>BERT Medium</th>
    <th>model = "bert-medium"; task="14to15"</th>
    <th>model = "bert-medium"; task="15to14"</th>
 </tr>
 <tr>
    <th>BERT Base</th>
    <th>model = "bert-base"; task="14to15"</th>
    <th>model = "bert-base"; task="15to14"</th>
 </tr>
 <tr>
    <th>CodeBert</th>
    <th>model = "codebert"; task="14to15"</th>
    <th>model = "codebert"; task="15to14"</th>
 </tr>
 <tr>
    <th>OCamlBert Large</th>
    <th>model = "ocamlbert-large"; task="14to15"</th>
    <th>model = "ocamlbert-large"; task="15to14"</th>
 </tr>
</table>

<h4 id="online"> Run the notebook on Kaggle </h4>
<ol>
  <li>First, make sure that you have a Kaggle account. (Free and convenient to create one.)</li>
  <li>Then, go to <a href="https://www.kaggle.com/code/tianyuhan2/inference-7fa4ae/edit"> Inference notebook </a> and click on Copy & Edit. Once you are in the notebook, log in. Then, in the right side bar, click on the Settings menu. If your account is yet to be phone verified, it should look like this picture below. Click on the <b>Get Phone Verified</b> and verify your account using your phone number.
  <p align="center">
  <img src="Image/sidebar.png" width="800" title="hover text" alt="Sidebar before phone verified..">
  </p>
  
  
  </li>
  <li>If your account is already phone verified, the Settings menu should look like this picture below. Then, under Accelerator, click on GPU. Also, make sure that the Internet switch is on.
  <p align="center">
  <img src="Image/sidebarafter.png" width="800" title="hover text" alt="Sidebar after phone verified.">
  </p>
  
  </li>
  <li>Run the notebook, enter the inputs as prompted, and get the results!</li>
</ol>

<h4 id="local"> Run the notebook on your own computer </h4>
<ol>
  <li>We used NVIDIA GeForce GTX 1650 as the GPU accelerator. If you have a different GPU, you may have to change the codes accordingly. Since we don't have various GPUs and we don't know what kind of errors would show up while running with a different GPU.</li>
  <li>Before running the notebook, please make sure that PyTorch along with cudatoolkit has been installed. To install, run <pre>conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge</pre> in your Anaconda Prompt. (There is more than one way to install these packages. More details can be found at https://pytorch.org/get-started/locally/).
  <p align="center">
  <img src="Image/condaprompt.png" width="800" title="hover text" alt="Installing packages.">
  </p>
  
  </li>
  <li>Then, open Jupyter Notebook installed on your local computer. (If there is not, please install Anaconda first. More details can be found at https://www.anaconda.com/). After loading, your default browser would show up with a page looking like this:
  <p align="center">
  <img src="Image/jupyter.png" width="800" title="hover text" alt="Homepage of Jupyter Notebook.">
  </p>
  </li>
  <li>Click Upload and upload your local inference notebook, along with the .zip file containing input data files. (The  <a href="https://github.com/GoudanHan/APLAS2022/blob/main/Script/inference-7fa4ae.ipynb">local version notebook</a> and the <a href="https://github.com/GoudanHan/APLAS2022/blob/main/Data/archive.zip">.zip file containing input data files</a> could be found at this repository.) Make sure that they are in the same directory. Don't unzip the file since our notebook will try to unzip it for you while running. (If they are not in the same directory, you may have to change the code in the notebook so that the notebook can find the .zip file and unzip it.)</li>
  <li>Open the notebook and click Cell -> Run All. Enter the inputs as prompted and get the results!
  <p align="center">
  <img src="Image/runlocally.png" width="800" title="hover text" alt="Homepage of Jupyter Notebook.">
  </p>
  
  </li>
  <li>On our end, when running the notebook, we have encountered two problems. Firstly, since we had only ran the notebook on Kaggle instead of locally, activating the GPU accelerator was not successful at first. After we installed the newest PyTorch package along with cudatoolkit, this problem was solved. The other problem was that when training the model, in the last cell, at the line <pre>outputs = model(b_input_ids, token_type_ids=None,  attention_mask=b_input_mask, labels=b_labels)</pre>, a runtime error message was displayed, saying "nll_loss_forward_reduce_cuda_kernel_2d_index" not implemented for "Int". We suspect that this is due to the GPU we used locally was different from the one on Kaggle. To solve this issue, we added the line <pre>b_labels = b_labels.to(torch.int64)</pre> right before this line, to do a type casting before feeding the input labels into the model.</li>
</ol>


<h3>Randomness</h3>
Please note the results are not stable due to randomness of initiliztion in training language models. Thus, we run each model three times and take the average to put in our paper. In the notebook, we provide only one instance of each model, thus you may observe some differences compared to the results in our paper.



<h2 id="nate"> NATE's models' accruacies (including OCaml and sherrloc) </h2>
<h3>Environment Installation & Setting up </h3>
<p> We provide an easy-to-use <a href="https://www.dropbox.com/s/nasq90j0p7jukbf/nate.ova?dl=0">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE</a>'s <a href="https://www.dropbox.com/s/b8a7nfwi8loiwvp/nate-artifact.ova?dl=0">virtual machine</a>, for people who want to reproduce NATE's experiments under the new metric. <p>The VM should already have everything installed; however, <b>it is possible that the graphical user interface of the VM fails to launch. We encountered the same issue while working on NATE's VM</b>. <em>The good news</em> is you just need the terminal to run the experiments. Press
<b><em>Alt</em> and <em>F3/F4/F2</em></b> together if no display or black screen, then you should see the terminal open.
<br>The user and password are both "<em>nate</em>".</p>

To activate the python virtualenv, type in the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
---------------------------------
<p>VM is now ready to reproduce the results. The commands of running the experiments are given in the following sections. <b>Notice: It is possible that accuracy of the same command <em>differ slightly</em> every time you execute it.</b></p>
<p>For models, <em>LOGISTIC</em>, <em>MLP-10</em> and <em>MLP-500</em>. We provide you commands for getting the new accuracy of the three ML models used by NATE. Each command takes about <em>10 to 30 minutes</em> to output the <em>final accuracy</em>, which relates to the number of features that you want the model to focus on.</p>
<table align="center">
  <tr>
    <th></th>
    <th>SP14->SP14</th>
    <th>SP14->FA15</th>
    <th>FA15->SP14</th>
    <th>FA15->FA15</th>
 </tr>
 <tr>
    <th>LOGISTIC</th>
    <th>./cts1414_l.sh</th>
    <th>./cts1415_l.sh</th>
    <th>./cts1514_l.sh</th>
    <th>./cts1515_l.sh</th>
 </tr>
 <tr>
    <th>MLP-10</th>
    <th>./cts1414_h10.sh</th>
    <th>./cts1415_h10.sh</th>
    <th>./cts1514_h10.sh</th>
    <th>./cts1515_h10.sh</th>
 </tr>
 <tr>
    <th>MLP-500</th>
    <th>./cts1414_h.sh</th>
    <th>./cts1415_h.sh</th>
    <th>./cts1514_h.sh</th>
    <th>./cts1515_h.sh</th>
 </tr>
</table>
<p>As NATE claims that <b>"+C(ontext)+T(ype)+S(ize)"</b> is the most powerful feature combination in error blaming. Hence, these three are the features we use for NATE's models in all experiments of this work.</p>
<p>We provide you a python script to get diagnosis/blaming accuracy of NATE's other models including <em>decision tree, random forest, Sherrloc</em> and <em>OCaml compiler</em>. Type <pre>python ./computeAccuracy.py</pre> to run the script.
<br>
Some messages will display on the terminal asking you to <em>properly</em> type the technique and dataset you want to use. Do <b>put</b> <em>single or double quotation marks</em> besides you answers as shown in the following example to make sure they can be read by the script:
<pre>
Please properly type the dataset you want to test. ('sp14' or 'fa15'): 'sp14'
Please properly type the technique you wish to use
        'decision-tree'
        'random-forest' 
        'sherrloc'
        'ocaml'
: "random-forest"
The accuracy is on its way...
The final accuracy is 38.79%
</pre>


<h2 id="graph">Graphs && Conclusion</h2>
<p>Following the above instructions, you can get the accuracy of any model used by NATE under <em>the new metric</em>, and be perfectly capable of reproduce similar graphs demonstrated in our paper. As every time you execute the command or the script, the final accuracy may differ slightly,but the results you will get is going to look <b>almost identical</b> to us. For those who are interested in our graphs and data, you can find the following Python scripts in our artifact submission via <a href="https://zenodo.org/record/7008941#.Yv8aXxzMJPY">Zenodo Link</a>, which the names of them corresponds to the figures 5 to 7 in our paper. 
</p>
<ul>
  <li><em>Accuracy of Type Error Localization Techniques.py</em></li>
  <li><em>Impact of type error threshold on blame accuracy.py</em></li>
  <li><em>Impacts on training loss.py</em></li>
</ul>
<p align="right"><a href="#header">↑Intro</a></p>
