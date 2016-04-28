name := "DarwinMinsky-project"

organization := "MBALearnsToCode"

version := "0.0.0"

scalaVersion := "2.10.6"   // latest Scala version compatible with Apache Spark

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.1",   // Apache Spark
  "org.scalanlp" %% "breeze" % "0.12",   // Breeze
  "org.scalanlp" %% "breeze-natives" % "0.12",   // Breeze natives
  "org.scalanlp" %% "breeze-viz" % "0.12",   // Breeze visualization
  "org.scalatest" %% "scalatest" % "2.2.1" % "test",
  "org.scalacheck" %% "scalacheck" % "1.11.5" % "test"
)

resolvers ++= Seq(
  "Sonatype Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/",
  "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/"
)

initialCommands := "import DarwinMinsky._"
