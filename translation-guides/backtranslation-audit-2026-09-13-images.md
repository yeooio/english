# 图片可见文字与图文对应审查

主审使用原始图片目视核对，PDF存储图经Poppler渲染后查看。范围：主稿实际调用的21个图片资产（7个方法/数据图、Oxford七图、CALCE/MIT六图、存储PDF一图），对应10个图环境。目录中未被主稿调用的旧图片不视为当前论文内容。以下中文为助手回译，图片没有单独冻结的中文文字版，不能伪造“中文图原文”。主审本轮未编辑图片。

## 可见文字回译与问题

|资产|主要英文文字的中文回译|五项审查结果|
|---|---|---|
|figures/fig1.png|Data acquisition=数据获取；Battery role assignment=电池角色分配；Prismatic/Cylindrical/Pouch=方形/圆柱形/软包；Full life cycle aging test=全寿命周期老化测试；Various charge-discharge protocols=多种充放电协议；charge/discharge rate=充/放电倍率；multi-step charge=多步充电；drive-cycle discharge=驾驶工况放电；Health indicators extraction=健康指标提取；Window Qdch=窗口Qdch；Energy efficiency eta=能量效率eta；MS-CCCT & PCC/SCC screening=MS-CCCT与PCC/SCC筛选；Time series of selected HIs=入选HI的时间序列；Health indicators splitting=健康指标划分；label=标签；window size=窗口大小；step:1=步长1；Four datasets dividing=四数据集划分；Train/Training=训练；Config./Configuration=配置；Eval./Evaluation=评价；others Cells=其他电池；Five models training, validating and testing=五模型训练、验证与测试；Storage comparison=存储比较；Accuracy/Generalization/Efficiency analysis=精度/泛化/效率分析；Cross-battery and cross-dataset evaluation=跨电池与跨数据集评价；FLOPs, Training time, Parameters, Model size=浮点运算次数、训练时间、参数量、模型大小；Experimental Validation=实验验证；Main results=主要结果；Comparison with four baseline models=与四种基线模型比较；Ablation=消融；Multi-scale DSConv and RAA=多尺度DSConv和RAA；Transfer=迁移；Source-only testing and few-shot adaptation=源域直接测试和少样本适应；Stability=稳定性；Initialization and convergence=初始化与收敛。模型图内文字同01.png。|①来源是既有图；②角色布局可能让读者认为训练/配置/评价三类互斥，正文配置电池也参加主对比，需明确；③Health indicators extraction、Health indicators splitting、Four datasets dividing、others Cells不自然；④不能由全寿命老化照片推断本文亲自实施实验；⑤范文可提供HI extraction搭配，但不能继承不同划分协议。见G01。|
|figures/fig2.png|Capacity(Ah)=容量；Cycle Number=循环编号；Voltage(V)=电压；Charge time(s)=充电时间；SOH=健康状态；(a)Oxford、(b)CALCE CS2、(c)CALCE CX2、(d)MIT/Severson。电池图例本应指各面板的电池。|①既有图；②(c)图例实际写CS2_36/37/38，与CALCE CX2标题不一致；③坐标英文自然，数值不能由回译重算；④无新增结论；⑤数据标识以本文来源为准。见G02。|
|figures/fig3.png|Voltage(V)=电压；Time(s)=时间；dQ/dV(mAh/V)=容量对电压的变化率；dT/dV(°C/V)=温度对电压的变化率；dT/dQ(°C/mAh)=温度对容量的变化率；Capacity(mAh)=容量。|①既有图；②(a)Time(s)只显示0–0.04，需核实时间单位/缩放，不能自行猜成小时；颜色条0–7800/7300没有可见变量名称，需明确对应循环量；③其他坐标语义清楚；④无夸大；⑤导数名称按公式而非按范文同义词替换。见G03。|
|figures/fig4_pccscc_print.png|SoH=健康状态；HI1–HI15=健康指标1–15；图中数字为相关系数；上方两图Cell1、下方两图Cell2及左右PCC/SCC由当前图题交代。|①源已有英文图；②新增图题对应与正文HI5的0.949/0.966及0.898/0.902取两位后相符；③SoH与正文SOH大小写可统一；④图中负值没有变成正值；⑤相关强度与方向不可混淆。这里只作可见标签与代表数值核对，不称逐一重算全部矩阵。|
|figures/01.png|Window split=窗口划分；HIs=健康指标；true SOH=真实SOH；pred SOH=预测SOH；Embed layer=嵌入层；Embeddings=嵌入表示；LayerNorm=层归一化；reshape=重塑形状；Linear=线性层；Add=相加；Gate=门控；Dropout=随机丢弃；FFN=前馈网络；SLFA features=SLFA特征；Transposing=转置；Turn/Back=转向/返回；L-DSConv=图中大核模块名；depth-Conv/point-Conv=图中深度/逐点卷积缩写；channel=通道；core structure=核心结构。|①既有图；②L-DSConv与正文DSConv-L不一致，Gate需与正文缩放操作区分；③Turn/Back不如Transpose/Inverse transpose准确；④不将Gate自动解释为已实现另一门控机制；⑤模块位置及命名必须与本文公式一致。见G04。|
|figures/02.png|pointwise conv filter=逐点卷积滤波器；depthwise conv filter=深度卷积滤波器；standard conv filter=标准卷积滤波器；channels=通道；Standard Conv=标准卷积；Standard DSConv=标准深度可分离卷积；DWConv=深度卷积；PWConv=逐点卷积；Linear=线性层；Add=相加。|①既有图；②1×5/1×31及2/3倍扩展与文字相符，但DSConv-L图内Add和额外Linear与正文模块边界不明确；③缩写可读；④无增强；⑤卷积内部位置不能因为范文画法而覆盖本文实现。见G05。|
|figures/fig3_3_attention_comparison.png|MatMul=矩阵乘法；Scale=缩放；Softmax=Softmax；ReLU²=ReLU平方；Linear=线性层；Add=相加；Softmax Global Attention=Softmax全局注意力；Linear Attention=线性注意力；Agent Attention=智能体注意力；Skim Local-Global Fusion Attention=图中Skim局部—全局融合注意力。|①既有图；②Skim/Slim与DSConv-L/DSConv-S及数据路径不一致；③Skim为拼写/命名错误；④复杂度n符号需要与正文n_a对应；⑤三篇的结构不能取代本文SLFA结构。见G06。|
|figures/Oxford/cell2.png–cell8.png（七张逐张查看）|SOH=健康状态；Error=误差；Reference=参考值；Cycle Number(100)=循环编号（100）；模型名MS-AgentNet、CNN-Transformer、Transformer、CNN-LSTM、LSTM保持。|①既有图；②SOH按0–1画图，(100)的单位乘数含义宜写清；③Reference在此为真实参考SOH，非参考文献；④图示仍可见其他模型更优的局部，不宣称全部最优；⑤趋势跟踪与总误差需分别解释。见G07。|
|figures/CSCXMIT/CS-37.png、CS-38.png、CX-37.png、CX-38.png、b3c13.png、b3c29.png（六张逐张查看）|SOH=健康状态；Error=误差；Reference=参考值；Cycle Number=循环编号；五种模型名不翻译。|①既有图；②标题电池名由TeX调用提供，与六个文件配对一致；③用词无需要更正项；④CX2_38尾部确有误差分化，但整颗MAPE不能自动充当局部阶段MAPE；⑤轨迹描述可对应范文，局部数字需本文证据。|
|figures/fig4_storage_scaling.pdf|Storage size(KB)=存储大小；Representation / hidden dimension=表示/隐藏维度；MS-A/CNN-T/Trans./CNN-L/LSTM=图中模型简称；(a)各宽度存储量，(b)不同宽度分布。|①既有图；②宽度16/32/64/128与正文相符，MS-AgentNet在所测宽度最低；③短标签自然；④这张图不表示推理延迟最低或已部署；⑤storage size与本文文件大小测量口径相符。|

## 具体问题及最小建议

- G01：流程图语言及协议呈现。`Health indicators extraction`建议`Health indicator extraction`；`Health indicators splitting`若指窗口切分，建议`Windowing of HI sequences`；`Four datasets dividing`建议按实际操作写`Data partitioning for the four datasets`；`others Cells`改`Other cells`。`Battery role assignment`下实际是三种封装，若表达电池类型，可写`Cell types`。训练/配置/评价框应明确配置电池也进入主报告范围；这一点需按正文协议统一图示。
- G02：数据图(c)标题CALCE CX2，但图例CS2_36/37/38。应先核对曲线源数据，再将正确电池标识写入，不能只凭标题擅自认定曲线就是CX2。
- G03：HI图(a)时间轴0–0.04 s和未命名颜色条需查看绘图源/原数据确认尺度。本报告不猜测正确单位，也不把不合理外观直接判为翻译错误。
- G04：架构图的`L-DSConv`应与正文`DSConv-L`一致；`Turn/Back`按实际操作可明确为`Transpose/Inverse transpose`。图中`Gate`与正文可学习缩放是否同一操作需要确认。
- G05：DSConv-L图画了模块内部残差Add，文字明确残差在Block级完成，图中还含Linear。应对实际实现统一图和公式，不能通过英文措辞掩盖结构差异。
- G06：图(d)的`Skim`应核对为正文已定义的`Slim`；图中DSConv-L在K/V支路，正文是DSConv-S先生成局部表示后进入RAA，且包含单独局部分支。不是仅改一个字母就完成的修复，需要统一模块路径和边界。
- G07：Oxford图的`Cycle Number(100)`可被读为“编号100”，若确为百次循环缩放，可写`Cycle number (×100)`。误差正负也需在图题/定义中明确真实值减预测值还是反向；本图图题目前只称估计结果，回译不会擅自补入符号定义。

以上是当前图文审查，不包含图源修改、复现实验或整页PDF排版验收。原图问题与中译英问题在总报告分别统计。
