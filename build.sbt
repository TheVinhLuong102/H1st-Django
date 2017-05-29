name := "DarwinMinskyWolfram-project"

organization := "MBALearnsToCode"

version := "0.0.0"

scalaVersion := "2.10.6"   // latest Scala version compatible with Apache Spark

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.1",   // Apache Spark
  "org.scalanlp" %% "breeze" % "0.12",   // Breeze
  "org.scalanlp" %% "breeze-natives" % "0.12",   // Breeze natives
  "org.scalanlp" %% "breeze-viz" % "0.12",   // Breeze visualization
  "org.scalactic" %% "scalactic" % "2.2.6",   // Scalactic
  "org.scalatest" %% "scalatest" % "2.2.6" % "test",   // ScalaTest
  "org.scalacheck" %% "scalacheck" % "1.13.0" % "test"   // ScalaCheck
)

resolvers ++= Seq(
  // for Breeze
  "Sonatype Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/",
  "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/"
)

initialCommands := "import DarwinMinskyWolfram._"
