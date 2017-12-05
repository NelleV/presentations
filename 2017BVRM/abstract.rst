The Scientific Python Tool stack for biomedical research

Whether it is for predicting the 3D structure of DNA, to develop new
clustering algorithm for time course gene expression data, or to analyse
terabytes of videos of cells exposed to toxins or drugs, the Scientific Python
Tool Stack presents a unique set of tools, easy to use yet flexible enough for
a wide range of applications.

I will describe in this talk three applications, and how our we leveraged some
of the tools of Scientific Python Tool Stack (numpy, scipy, Matplotlib,
scikit-learn, autograd…) for better and faster research. First, I will talk
about Pastis, a tool to infer 3D structures of DNA from contact map matrix,
and how we moved from a C++ code base to a Python one without lost of speed.
Second, I will present how using appropriate data structures for matrix
balancing algorithms, used for preprocessing of DNA contact maps can be
competitive with parallized C++ code. Third, I will show how autograd helped
us solved complicated optimization problems without having to tediously
derivate complicated functions by hand, allowing us to do stability analysis
on clustering of time course gene expression data.
