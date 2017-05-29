name := "DarwinMinskyWolfram-project"

organization := "MBALearnsToCode"

version := "0.0.0"

scalaVersion := "2.11.11"   // latest Scala version compatible with Apache Spark

libraryDependencies ++= Seq(
  // Spark
  "org.apache.spark" %% "spark-core" % "2.1.1",

  // Hadoop
  "org.apache.hadoop" % "hadoop-client" % "2.8.0",

  // Breeze
  "org.scalanlp" %% "breeze" % "0.13.1",
  "org.scalanlp" %% "breeze-natives" % "0.13.1",
  // "org.scalanlp" %% "breeze-viz" % "0.13.1",

  // ScalaCheck
  "org.scalacheck" %% "scalacheck" % "1.13.4" % "test",

  // Scalactic
  "org.scalactic" %% "scalactic" % "3.0.1",

  // ScalaTest
  "org.scalatest" %% "scalatest" % "3.0.1" % "test"
)

resolvers ++= Seq(
  // for Breeze
  "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/",
  "Sonatype Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/"
)

initialCommands := "import DarwinMinskyWolfram._"
