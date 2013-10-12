from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

prompt = lambda: raw_input('\nPress Enter to continue test:');

def Test(tests=None):
   if tests != None:
      for test in tests:
         test();
      print "\nTests complete\n"

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
   print "\nSimpleHyperTreeTest complete"

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

   prompt();
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

   prompt();
   print "\nTail 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   prompt();
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

   prompt();
   print "\nTail 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   prompt();
   print "\nTail 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(3);
   hyperTreeRoot.Show();

   print "\nTailTest complete"

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

   prompt();

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

   prompt();

   print "\nHead 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   prompt();

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

   prompt();
   print "\nHead 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   prompt();
   print "\nHead 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(3);
   hyperTreeRoot.Show();
   print "\nHeadTest complete";

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
   prompt();

   print "\nPrime 2 HyperTree:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   prompt();
   print "\nPrime 3 HyperTree:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';
   prompt();

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

   prompt();
   print "\nPrime 2 HyperTree 2:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   prompt();
   print "\nPrime 3 HyperTree 2:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   prompt();
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

   prompt();
   print "\nPrime 2 HyperTree 3:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   prompt();
   print "\nPrime 3 HyperTree 3:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   print "\nPrimeTest complete";

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

   prompt();
   print "\nHyperTree Prime, Prime:";
   primeTree = primeTree.Prime();
   primeTree.Show();

   prompt();
   print "\nHyperTree Prime, Tail:";
   primeTailTree = hyperTreeRoot.Prime();
   primeTailTree.Tail();
   primeTailTree.Show();

   prompt();
   print "\nHyperTree Prime, Tail, Prime:";
   primeTailPrimeTree = primeTailTree.Prime();
   primeTailPrimeTree.Show();

   prompt();
   print "\nHyperTree Prime, Tail, Prime, Prime:";
   primeTailPrimePrimeTree = primeTailPrimeTree.Prime();
   primeTailPrimePrimeTree.Show();

   prompt();
   print "\nHyperTree Prime, Tail, Prime, Head:";
   primeTailPrimeTree.Head();
   primeTailPrimeTree.Show();

   print "\nCombinedTest complete";

def RunTests():
   # put any function from above into here:
   TestsToRun = [SimpleHyperTreeTest, TailTest, HeadTest, PrimeTest, CombinedTest];
   Test(TestsToRun);

