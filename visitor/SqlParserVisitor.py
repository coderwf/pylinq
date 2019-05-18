# Generated from SqlParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from parser.SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.

class SqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#root.
    def visitRoot(self, ctx:SqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#sqlStatements.
    def visitSqlStatements(self, ctx:SqlParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#sqlStatement.
    def visitSqlStatement(self, ctx:SqlParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#emptyStatement.
    def visitEmptyStatement(self, ctx:SqlParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#dmlStatement.
    def visitDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#timestampValue.
    def visitTimestampValue(self, ctx:SqlParser.TimestampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#intervalExpr.
    def visitIntervalExpr(self, ctx:SqlParser.IntervalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#intervalType.
    def visitIntervalType(self, ctx:SqlParser.IntervalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#functionParameter.
    def visitFunctionParameter(self, ctx:SqlParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#simpleSelect.
    def visitSimpleSelect(self, ctx:SqlParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:SqlParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#orderByClause.
    def visitOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#orderByExpression.
    def visitOrderByExpression(self, ctx:SqlParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#tableSources.
    def visitTableSources(self, ctx:SqlParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#tableSourceBase.
    def visitTableSourceBase(self, ctx:SqlParser.TableSourceBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#tableSourceNested.
    def visitTableSourceNested(self, ctx:SqlParser.TableSourceNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#atomTableItem.
    def visitAtomTableItem(self, ctx:SqlParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:SqlParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#innerJoin.
    def visitInnerJoin(self, ctx:SqlParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#straightJoin.
    def visitStraightJoin(self, ctx:SqlParser.StraightJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#outerJoin.
    def visitOuterJoin(self, ctx:SqlParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#queryExpression.
    def visitQueryExpression(self, ctx:SqlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#querySpecification.
    def visitQuerySpecification(self, ctx:SqlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectSpec.
    def visitSelectSpec(self, ctx:SqlParser.SelectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectElements.
    def visitSelectElements(self, ctx:SqlParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectStarElement.
    def visitSelectStarElement(self, ctx:SqlParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:SqlParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:SqlParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:SqlParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#fromClause.
    def visitFromClause(self, ctx:SqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#groupByItem.
    def visitGroupByItem(self, ctx:SqlParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#limitClause.
    def visitLimitClause(self, ctx:SqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#fullId.
    def visitFullId(self, ctx:SqlParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#tableName.
    def visitTableName(self, ctx:SqlParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#fullColumnName.
    def visitFullColumnName(self, ctx:SqlParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#mysqlVariable.
    def visitMysqlVariable(self, ctx:SqlParser.MysqlVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#uid.
    def visitUid(self, ctx:SqlParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#simpleId.
    def visitSimpleId(self, ctx:SqlParser.SimpleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#dottedId.
    def visitDottedId(self, ctx:SqlParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:SqlParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#stringLiteral.
    def visitStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:SqlParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:SqlParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#nullNotnull.
    def visitNullNotnull(self, ctx:SqlParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#constant.
    def visitConstant(self, ctx:SqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#simpleDataType.
    def visitSimpleDataType(self, ctx:SqlParser.SimpleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#spatialDataType.
    def visitSpatialDataType(self, ctx:SqlParser.SpatialDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#convertedDataType.
    def visitConvertedDataType(self, ctx:SqlParser.ConvertedDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#uidList.
    def visitUidList(self, ctx:SqlParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#tables.
    def visitTables(self, ctx:SqlParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expressions.
    def visitExpressions(self, ctx:SqlParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expressionsWithDefaults.
    def visitExpressionsWithDefaults(self, ctx:SqlParser.ExpressionsWithDefaultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#constants.
    def visitConstants(self, ctx:SqlParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#simpleStrings.
    def visitSimpleStrings(self, ctx:SqlParser.SimpleStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#userVariables.
    def visitUserVariables(self, ctx:SqlParser.UserVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#defaultValue.
    def visitDefaultValue(self, ctx:SqlParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#currentTimestamp.
    def visitCurrentTimestamp(self, ctx:SqlParser.CurrentTimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx:SqlParser.ExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ifExists.
    def visitIfExists(self, ctx:SqlParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ifNotExists.
    def visitIfNotExists(self, ctx:SqlParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:SqlParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx:SqlParser.AggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:SqlParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx:SqlParser.UdfFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:SqlParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx:SqlParser.DataTypeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx:SqlParser.ValuesFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:SqlParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx:SqlParser.CharFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx:SqlParser.PositionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx:SqlParser.SubstrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx:SqlParser.TrimFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx:SqlParser.WeightFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx:SqlParser.ExtractFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx:SqlParser.GetFormatFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx:SqlParser.CaseFuncAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx:SqlParser.AggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:SqlParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#functionArgs.
    def visitFunctionArgs(self, ctx:SqlParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#functionArg.
    def visitFunctionArg(self, ctx:SqlParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#isExpression.
    def visitIsExpression(self, ctx:SqlParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#notExpression.
    def visitNotExpression(self, ctx:SqlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#logicalExpression.
    def visitLogicalExpression(self, ctx:SqlParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:SqlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx:SqlParser.SoundsLikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:SqlParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#inPredicate.
    def visitInPredicate(self, ctx:SqlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#subqueryComparasionPredicate.
    def visitSubqueryComparasionPredicate(self, ctx:SqlParser.SubqueryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#binaryComparationPredicate.
    def visitBinaryComparationPredicate(self, ctx:SqlParser.BinaryComparationPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#likePredicate.
    def visitLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:SqlParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:SqlParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#subqueryExpressionAtom.
    def visitSubqueryExpressionAtom(self, ctx:SqlParser.SubqueryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:SqlParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:SqlParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx:SqlParser.BinaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:SqlParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx:SqlParser.BitExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:SqlParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:SqlParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#existsExpressionAtom.
    def visitExistsExpressionAtom(self, ctx:SqlParser.ExistsExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx:SqlParser.IntervalExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#unaryOperator.
    def visitUnaryOperator(self, ctx:SqlParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:SqlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:SqlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#bitOperator.
    def visitBitOperator(self, ctx:SqlParser.BitOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#mathOperator.
    def visitMathOperator(self, ctx:SqlParser.MathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx:SqlParser.IntervalTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#dataTypeBase.
    def visitDataTypeBase(self, ctx:SqlParser.DataTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:SqlParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:SqlParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)



del SqlParser