from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

def Test(tests=None):
   for test in tests:
      eval(test + '()');

def SimpleHyperTreeTest():
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))

   print "Original HTML as soup tree:";
   print soup.prettify();
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree:";
   hyperTreeRoot.Show();

def TailTest():
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree:";
   hyperTreeRoot.Show();

   print "\nTail HyperTree:";
   hyperTreeRoot.Tail();
   hyperTreeRoot.Show();

   doc = ['<head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       ''];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree 2:";
   hyperTreeRoot.Show();

   print "\nTail HyperTree 2:";
   hyperTreeRoot.Tail();
   hyperTreeRoot.Show();

   print "\nTail 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   doc = ['<head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>'];
   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree 3:";
   hyperTreeRoot.Show();

   print "\nTail HyperTree 3:";
   hyperTreeRoot.Tail();
   hyperTreeRoot.Show();

   print "\nTail 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   print "\nTail 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(3);
   hyperTreeRoot.Show();

def HeadTest():
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree:";
   hyperTreeRoot.Show();

   print "\nHead HyperTree:";
   hyperTreeRoot.Head();
   hyperTreeRoot.Show();

   doc = ['<head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       ''];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree 2:";
   hyperTreeRoot.Show();

   print "\nHead HyperTree 2:";
   hyperTreeRoot.Head();
   hyperTreeRoot.Show();

   print "\nHead 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   doc = ['<head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>',
       '<extra><p id="stuff" align="left">This is extra </extra>'];
   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree 3:";
   hyperTreeRoot.Show();

   print "\nHead HyperTree 3:";
   hyperTreeRoot.Head();
   hyperTreeRoot.Show();

   print "\nHead 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   print "\nHead 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(3);
   hyperTreeRoot.Show();

def PrimeTest():
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree:";
   hyperTreeRoot.Show();

   print "\nPrime HyperTree:";
   prime = hyperTreeRoot.Prime();
   prime.Show();

   print "\nPrime 2 HyperTree:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   print "\nPrime 3 HyperTree:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   doc = ['<head></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       ''];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree 2:";
   hyperTreeRoot.Show();

   print "\nPrime HyperTree 2:";
   prime = hyperTreeRoot.Prime();
   prime.Show();

   print "\nPrime 2 HyperTree 2:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   print "\nPrime 3 HyperTree 2:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   doc = ['<head></head>',
       '<body><p id="firstpara" align="center">This is paragraph.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</body>'];
   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree 3:";
   hyperTreeRoot.Show();

   print "\nPrime HyperTree 3:";
   prime = hyperTreeRoot.Prime();
   prime.Show();

   print "\nPrime 2 HyperTree 3:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   print "\nPrime 3 HyperTree 3:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

def CombinedTest():

   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))

   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree:";
   hyperTreeRoot.Show();

   print "\nHyperTree Prime:";
   primeTree = hyperTreeRoot.Prime();
   primeTree.Show();

   print "\nHyperTree Prime, Prime:";
   primeTree = primeTree.Prime();
   primeTree.Show();

   print "\nHyperTree Prime, Tail:";
   primeTailTree = hyperTreeRoot.Prime();
   primeTailTree.Tail();
   primeTailTree.Show();

   print "\nHyperTree Prime, Tail, Prime:";
   primeTailPrimeTree = primeTailTree.Prime();
   primeTailPrimeTree.Show();

   print "\nHyperTree Prime, Tail, Prime, Prime:";
   primeTailPrimePrimeTree = primeTailPrimeTree.Prime();
   primeTailPrimePrimeTree.Show();

   print "\nHyperTree Prime, Tail, Prime, Head:";
   primeTailPrimeTree.Head();
   primeTailPrimeTree.Show();

