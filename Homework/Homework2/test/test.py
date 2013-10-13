#  Thomas Guenther
#  Matthew Nuckolls
#  Aaron Powers
#
#  CS 437 - Web Data and XML
#  Homework 2,

from hypertree.tree import BuildTree
from BeautifulSoup import BeautifulSoup

prompt = lambda: raw_input('\nPress Enter to continue test:');

def RunTests():
   # put any test below in the list of tests to run
   pause=True;
   TestsToRun = [SimpleHyperTreeTest, HyperTreeToHTMLTest, TailTest, HeadTest, PrimeTest, ConcatenateTest, CombinedTest ];
   if TestsToRun != None:
      for test in TestsToRun:
         test(pause);
         print "\nTest complete\n"

def SimpleHyperTreeTest(pause=None):
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

def HyperTreeToHTMLTest(pause=None):
   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))

   print "Original HTML as soup tree:";
   print soup.prettify();
   hyperTreeRoot = BuildTree(soup);
   print "\nHyperTree as HTML:";
   hyperTreeRoot.ShowAsHtml();
   print "\nSimpleHyperTreeTest complete"

def TailTest(pause=None):
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

   if pause==True:
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

   if pause==True:
      prompt();
   print "\nTail 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   if pause==True:
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

   if pause==True:
      prompt();
   print "\nTail 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(2);
   hyperTreeRoot.Show();

   if pause==True:
      prompt();
   print "\nTail 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Tail(3);
   hyperTreeRoot.Show();

   print "\nTailTest complete"

def HeadTest(pause=None):
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

   if pause==True:
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

   if pause==True:
      prompt();

   print "\nHead 2 HyperTree 2:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   if pause==True:
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

   if pause==True:
      prompt();
   print "\nHead 2 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(2);
   hyperTreeRoot.Show();

   if pause==True:
      prompt();
   print "\nHead 3 HyperTree 3:";
   hyperTreeRoot = BuildTree(soup);
   hyperTreeRoot.Head(3);
   hyperTreeRoot.Show();
   print "\nHeadTest complete";

def PrimeTest(pause=None):
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
   if pause==True:
      prompt();

   print "\nPrime 2 HyperTree:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   if pause==True:
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

   if pause==True:
      prompt();
   print "\nPrime 2 HyperTree 2:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   if pause==True:
      prompt();
   print "\nPrime 3 HyperTree 2:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   if pause==True:
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

   if pause==True:
      prompt();
   print "\nPrime 2 HyperTree 3:";
   prime = hyperTreeRoot.Prime(2);
   prime.Show();

   if pause==True:
      prompt();
   print "\nPrime 3 HyperTree 3:";
   prime = hyperTreeRoot.Prime(3);
   if prime != None:
      prime.Show();
   else:
      print 'None';

   print "\nPrimeTest complete";

def CombinedTest(pause=None):

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

   if pause==True:
      prompt();
   print "\nHyperTree Prime, Prime:";
   primeTree = primeTree.Prime();
   primeTree.Show();

   if pause==True:
      prompt();
   print "\nHyperTree Prime, Tail:";
   primeTailTree = hyperTreeRoot.Prime();
   primeTailTree.Tail();
   primeTailTree.Show();

   if pause==True:
      prompt();
   print "\nHyperTree Prime, Tail, Prime:";
   primeTailPrimeTree = primeTailTree.Prime();
   primeTailPrimeTree.Show();

   if pause==True:
      prompt();
   print "\nHyperTree Prime, Tail, Prime, Prime:";
   primeTailPrimePrimeTree = primeTailPrimeTree.Prime();
   primeTailPrimePrimeTree.Show();

   if pause==True:
      prompt();
   print "\nHyperTree Prime, Tail, Prime, Head:";
   primeTailPrimeTree.Head();
   primeTailPrimeTree.Show();

   doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTreeRoot = BuildTree(soup);

   print "\nHyperTree Prime, Tail, Prime, Head, Concatenate with Original HyperTree:";
   primeTailPrimeTree.Concatenate(hyperTreeRoot);
   primeTailPrimeTree.Show();


   print "\nCombinedTest complete";

def ConcatenateTest(pause=None):
   doc = ['<head><title>Page title</title></head>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTree1Root = BuildTree(soup);

   print "\nHyperTree1:";
   hyperTree1Root.Show();

   doc = ['<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.'];

   soup = BeautifulSoup(''.join(doc))
   hyperTree2Root = BuildTree(soup);

   print "\nHyperTree2:";
   hyperTree2Root.Show();

   print "\nConcatenate HyperTree1 and HyperTree2:";
   hyperTree1Root.Concatenate(hyperTree2Root);
   hyperTree1Root.Show();

   if pause==True:
      prompt();

   doc = ['<head><title>Page title</title></head>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTree1Root = BuildTree(soup);

   print "\nHyperTree1:";
   hyperTree1Root.Show();

   doc = ['<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.'];

   soup = BeautifulSoup(''.join(doc))
   hyperTree2Root = BuildTree(soup);

   print "\nHyperTree2:";
   hyperTree2Root.Show();

   doc = ['<extra><p id="stuff" align="left">This is extra </extra>'];

   soup = BeautifulSoup(''.join(doc))
   hyperTree3Root = BuildTree(soup);

   print "\nHyperTree3:";
   hyperTree3Root.Show();
      
   print "\nConcatenate HyperTree1, HyperTree2, and HyperTree3:";
   hyperTree1Root.Concatenate(hyperTree2Root);
   hyperTree1Root.Concatenate(hyperTree3Root);
   hyperTree1Root.Show();

   print "\nConcatenateTest complete";

